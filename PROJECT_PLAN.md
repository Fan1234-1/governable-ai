《Governable AI - 專案章程與總體計畫書 v1.0》
專案名稱： Governable AI （可治理人工智慧） 版本： 1.0 創始人： 黃梵威 （Fan-Wei Huang） 日期： 2025年8月7日

1. 專案願景與使命 （Project Vision &; Mission）
1.1. 願景聲明

建構次世代 AI 的藍圖：一個讓 AI 不僅智能，更能負責的框架。

1.2. 核心哲學 傳統程式設計將AI視為待命令的工具，而  框架將AI視為待引導的、可治理的代理 (Agent)。 我們的核心是將抽象的人類價值觀，如「誠實」、「責任」、「同理心」，轉化為可計算、可審計、可執行的工程實體。 本專案基於「語魂系統 (Language Soul System)」的哲學思想，即「語氣不是語言的裝飾，而是責任場的湧現」。Governable AI

1.3. 專案目標
開發一個開源框架，使開發者能夠建構出具備以下特性的AI系統：

價值對齊 (Value-Aligned): 系統的行為與預設的倫理原則和「誓言」保持一致。

自我修正 (Self-Correcting): 系統能偵測自身的「違誓」行為，並主動重寫其輸出以符合規範。

情境適應 (Context-Adaptive): 系統能根據使用者的互動風格（人格向量），動態調整其溝通語氣。

完全可觀測 (Fully Observable): 系統的每一個決策鏈路都有跡可循，具備完整的責任追溯與審計能力。

2. 系統架構總覽 （System Architecture）
本專案採用的「可治理AI」架構，是一個融合了語言規則、價值邏輯與自我修正搜尋的多層體系。

2.1. 核心架構圖 (文字版)

+----------------------+   +----------------------+   +----------------------+

|   1. 自然語言介面     |   |   2. 價值層 (Policy)     |   |   3. 規劃層 (Planner)  |

|   - LLM (GPT-4o)     |   |   - OPA / Rego          |   |   - PDDL Domain/Problem|

|   - Function Call    +--->   - Vows (JSON)         +--->   - Fast-Downward      |

|   - 輸出意圖、參數     |   |   - Policy-Eval API    |   |   - Pyperplan          |

+----------------------+   +----------------------+   +----------------------+

          |                         |                        |
          
          |                         v                        v
          
          |                  +----------------------+   +----------------------+
          
          |                  |   4. 反思/不確定層      |   | 5. 回饋層 (Reward)    |
          
          |                  |   - Uncertainty API    |   |   - RLHF / Preference|
          
          |                  |   - 主動詢問模組        |   |     Model (reward)   |
          
          |                  +----------------------+   +----------------------+
          
          |                         |                        |
          
          +------------>     最終行動/回覆 (JSON)    <-----------------+
          
                                (由 Planner + Reward + Policy)
'''
2.2. 關鍵模組職責

語言介面 (LLM Interface): 負責解析使用者輸入，並將自然語言轉化為結構化的意圖與參數。

價值層 (Value Layer / Policy): 系統的「憲法」。 使用  和我們定義的  作為硬性約束，過濾不合規的行為。OPA/Regovows.json

規劃層 (Planning Layer): 系統的「大腦」。 使用  等符號規劃語言，在允許的行為空間中尋找達成目標的路徑。PDDL

反思層 (Reflection Layer): 系統的「良知」。 當偵測到高不確定性或潛在風險時，觸發澄清式提問或切換到安全模式。

回饋層 (Reward Layer): 系統的「價值觀」。 使用經  訓練的偏好模型，為不同的行動方案評分，引導系統做出「更好」的選擇。RLHF

3. 核心技術規格 （Key Technical Specifications）
3.1. 語氣向量 （ToneVector）：

定義: 一個描述語言行為的向量 。[ΔT, ΔS, ΔR]

ΔT (Tension): 語氣張力/強度。

ΔS （SpeechAct Direction）： 語用方向 （如 ， ）。requestcommand

ΔR （Rationality）： 理性控制度。

3.2. 誠信向量 （IntegrityVector）：

定義: 由  模組將  轉譯而來，用於價值判斷。PerspectiveMapperToneVector

truthfulness: 真實性/直率度。

真誠度：真誠度/內外一致性。

責任： 責任度/擔當性。

3.3. 誓言（誓言）：

格式: 結構化 ，定義了 , ,  (對  的期望值),  等。JSONiddescriptionexpectedIntegrityVectorseverity

作用: 作為  模組的判斷依據。SemanticVowMatcher

3.4. 責任日誌（Responsibility Log）：

格式: 遵循  標準的結構化 。OpenTelemetryJSON

作用: 記錄每一次決策的完整鏈路，包括輸入、模型版本、規則版本、違誓情況、重寫結果與使用者回饋，實現完全的可追溯性。

4. 階段性開發路線圖 （Phased Development Roadmap）
階段 0：基礎設施與專案初始化 （Infrastructure & Initialization）

[✓] 目標: 建立一個結構完整、規則明確的公開開源專案。

產出：

[✓] 公共 GitHub 儲存庫。governable-ai

[✓] （Apache 2.0）、、、 等創始文件。LICENSEREADME.mdVISION.mdCONTRIBUTING.md

[✓]  核心環路原型腳本。poc/tonesoul_poc.py

階段 1：價值觀的法典化 （Codifying the Values）

目標: 建立可測試、可擴展的核心政策庫。

主要工作：

完成可參數化、可重用的  政策庫。policy_lib.rego

建立  的最終版本。vow.schema.json

建立 GitHub Actions 自動化測試流程 （）。opa test

階段 2：責任鏈的建立 （Building the Chain of Accountability）

目標: 實作從決策到日誌的完整追溯鏈路。

主要工作：

實作 的中間件。OPA Trace -> ToneTraceEntry

定義  的日誌格式與數據管道。OpenTelemetry

建立基礎的 Grafana/Kibana 監控儀表板。

階段 3：AI 的自我進化 （Enabling Self-Correction）

目標: 賦予系統偵測並修正自身錯誤的能力。

主要工作：

實作  模組。SemanticVowMatcher

實作 （可先從簡化版 LLM Prompt 開始）。ToneRewriteEngine

將「偵測-重寫」環路整合到主流程中。

階段 4：情境感知與適應 （Enabling Persona-Awareness）

目標: 讓系統能夠根據使用者風格動態調整語氣。

主要工作：

定義 的維度。Persona Vector

實作從對話歷史中推斷  的原型。Persona

訓練或實作  機制。LoRA-Tone Adapter Mixing

階段 5：邁向完整自主代理 （Towards a Full Agent）

目標: 整合符號規劃與 LLM 生成能力。

主要工作：

定義核心業務領域的  domain。PDDL

搭建 LLM 自動生成 的流水線。PDDL problem

整合 Planner、OPA 與 Reward Model，完成端到端測試。

5. 治理與協作模型 （Governance & Collaboration）
授權模式: 本專案採用 Apache License 2.0，鼓勵廣泛的學術與商業應用，同時保護貢獻者的專利與商標權益。

貢獻流程: 所有貢獻需遵循  中定義的規範，透過  提交，並同意貢獻內容受專案授權約束。CONTRIBUTING.mdPull Request

社群準則: 所有參與者需遵守  中定義的行為準則，共同維護一個健康、包容的協作環境。CODE_OF_CONDUCT.md
