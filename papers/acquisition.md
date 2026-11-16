# Lawful acquisition protocol

1. Verify the canonical publisher/archive record and version.
2. Confirm a redistribution license compatible with a **public** GitHub repository. Reading rights and downloading rights do not automatically permit rehosting.
3. Fetch only a verified URL, preferably official OA repository or author-authorized preprint.
4. Record `ACQUISITION.json`: paper_id, URL, date, version, content_type, sha256, license_url and verifier.
5. Save original PDF/HTML/TeX without altering author content. For copyright-restricted works preserve the source URL and original analytical review only.
6. Never put third-party API credentials or personal data in the corpus. Do not use paywall circumvention.

**Environment limitation (2026-11-16):** GitHub connector supports text repository writes but not unrestricted binary publisher PDF uploads. The source tree is therefore a verified-acquisition backlog, not a claim of PDF completion.

### Lawful repositories to check
ACL Anthology for ACL papers; PMLR and NeurIPS proceedings for permitted machine-learning papers; arXiv for authors' preprints (verify license per item); institutional repositories; publisher open-access pages. Always check license and paper version.
