# Research integrity and paper review specification

## Artifact policy
Every paper has a stable ID, canonical venue/DOI URL, source acquisition status, evidence-access level, category, individual review and linked mechanisms. Do not store publisher PDFs unless licensing/distribution permits redistribution in this public repository. A PDF available to read is not necessarily licensed for republication.

## Review structure (mandatory)
Identity and access; research question; studied population/problem; method and controls; precise findings; assumptions; limitations and confounds; disagreement/negative findings; implications for Routin; proposed algorithm/data contract; integration with other papers; falsifiable tests; confidence/status; unresolved questions; reproduction/source links.

## Confidence labels
`verified_full_text`: reviewed entire accessible paper; `partial_text`: reviewed a section; `abstract_only`: bibliographic abstract and metadata; `structured_extract`: scholarly extraction, needs full-text cross-check; `source_unavailable`: only title/metadata.
No 'read' claim for an abstract. If license unclear, store acquisition manifest and official link; fetch locally only after license review. Maintain retrieval date and SHA256 for genuine local full-text sources.

## Review discipline
Do not confuse: source claim with Routin result; observed effect with causal mechanism; theory with controlled effect; benchmark with real-world benefit; official docs with psych evidence. Deduplicate paper variants and avoid numerical novelty scores without prior-art mapping.

## Required artifacts
A review file per paper. A source pointer `papers/<category>/<id>/SOURCE.md`. A central catalog and acquisition utility. A mechanism map linking multiple papers to each decision. A testing plan with baselines and counterexamples.