# Mutual Grounding, Articulation Work and Coordination Cost

**Sources:** Schmidt & Bannon (1992), Clark & Brennan (1991), Erickson et al. (2008), Horvitz (1999), Garcia-Molina & Salem (1987).

## Derivation

A competent secretary does not merely perform tasks. They undertake *articulation work*: ensuring distributed activity remains coordinated when participants, plans, resources and constraints change. Communication theory adds a further stage: sending a message differs from achieving adequate mutual understanding. The coordination objective is not minimizing words or interactions for one party but reducing the collaborative effort required to reach a usable agreement.

A unilateral scheduler can reduce the principal's apparent effort while transferring large, repeated coordination costs to counterparties. That is a second-order externality and a potential reputational failure.

## CoordinationEpisode domain object

A coordination episode tracks:
- principal, counterparty and source identities, each with resolution confidence;
- requested outcome, proposed alternatives, social constraints and accepted terms;
- last message or provider receipt, separately from evidence of mutual understanding;
- next expected response or handoff, latest useful decision time and source coverage;
- current owner and status: proposed, transmitted, delivered, interpreted, counterproposed, accepted, rejected, waiting, disputed or completed;
- cost of follow-up, nonresponse and unnecessary counterpart interruption.

## Protocol

Before sending, validate the actual user purpose and current grant. On provider acceptance, record only a sent effect. On an explicit response, update the agreement state; on silence, evaluate whether a response was expected and whether the source coverage is fresh. Ask for repair when the recipient's interpretation materially differs from the requested outcome. Never equate opened, received or replied with mutually agreed.

## Least collaborative effort as a hypothesis

Estimate the costs of:
- user clarification;
- counterparty clarification;
- waiting or delayed work;
- wrong assumptions and repair;
- repeated follow-up or renegotiation;
- communication style mismatch.

Minimize avoidable *joint* coordination cost while preserving consent, truthful reporting and valid authority. No optimization over an inferred counterparty utility function without reliable evidence.

## Falsification

Compare shortest-message drafting, send-and-close, and grounded handoff protocols. Measure verified agreements, number of repair turns, false meeting acceptance, user and counterparty effort, and interpersonal complaints. If grounding introduces excessive overhead without outcome benefits for low-risk interactions, narrow it to consequential cases.