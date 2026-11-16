# ADR-0004 — Attention policy cannot grant action authorization

Status: proposed.
A highly relevant request is not equivalent to permission to send messages. User preference inference cannot expand grants. Enforce hard current action grants independently of optimized attention/delegation proposals.

Trade-offs: more approval pauses for some operations; lower unauthorized-effect risk. Verify via injection, revoked scope and adversarial action tests. Sources: mixed-initiative HCI, human-AI guidelines and transactional workflow engineering.