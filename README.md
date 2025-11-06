# Governable AI - DDD & Policy-as-Code

## Guardian Protocol v1.0 - Governance Layer

本倉庫是治理層，負責通過 DDD 分解和 Policy-as-Code 實現可治理的 AI 系統。

---

## Domain-Driven Design Bounded Contexts

### DDD Domains

| Domain | Responsibility | Integration |
|--------|---|---|
| ValueLogic | Price Conversion & Integrity | Integrity Layer |
| PolicyEngine | Policy Execution & Logging | Governance |
| AgentGovernance | AI Agent Management | Guardian Protocol |
| DecisionTracing | Decision Trace & Immutable Log | Philosophy |

---

## Policy-as-Code Framework

```typescript
interface PolicyRule {
  id: string;              // Policy ID
  context: string;         // DDD Context
  condition: Condition;    // Trigger Condition
  action: Action;          // Execution Action
  priority: 'P0'|'P1'|'P2'|'P3'|'P4';
  mode: 'strict'|'soft';
}

interface GovernanceGate {
  level: 'P0'|'P1'|'P2'|'P3'|'P4';
  approvals_required: number;
  policies: PolicyRule[];
  consensus_threshold: number;
}
```

---

## Integration with Guardian Protocol

1. Integrity -> Governance: VowDefinition -> Policy Priority
2. Governance -> Responsibility: Decisions -> Responsibility Logs
3. Governance -> Philosophy: Governance Logs -> Knowledge Galaxy

---

## Version & Maintenance

- Framework: Guardian Protocol v1.0
- Last Updated: 2025-11-06
- License: Apache-2.0
- Core Function: DDD Decomposition & Policy-as-Code
