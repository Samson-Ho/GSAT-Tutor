# Publish GSAT-Tutor to OpenAI's universal Plugin Directory

This repository prepares a **skills-only plugin**, not a Custom GPT or GPT
Store entry. A GitHub push does not publish it. The owner must upload, submit
for review, and publish the approved version in the OpenAI dashboard before
directory installation can become available on supported ChatGPT web,
iPhone/iPad, desktop, and Codex surfaces. Account, organization, country, and
client availability still apply.

## What the repository handles

- Root `plugin.json` follows [Agent Plugins 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).
  Shared identity/version metadata matches `.claude-plugin/plugin.json`.
  OpenAI presentation lives in `extensions.com.openai.interface`; root
  `skills/` is discovered automatically, without a manifest `skills` field.
- Five shared subjects use packaged Markdown references and host resource
  readers. PDFs remain bundled. Local PDF tools and the Python vocabulary
  helper are optional; exact inaccessible images/rubrics require student
  material or clearly labelled provisional guidance.
- The original Claude manifest and `gsat-tutor-marketplace` catalog retain
  their names and `source: "./"`. No native marketplace is added.
- No `.codex-plugin/plugin.json` is needed. The
  [current package guide](https://developers.openai.com/plugins/build/plugins)
  makes it an optional fallback; inline `extensions.com.openai` replaces that
  overlay rather than merging it. Older local workflows still have the
  existing Claude-compatible files. OpenAI public uploads use only the
  portable manifest, independently of Claude files.
- Listing category is **Education & Research**, a documented accepted value;
  `Education` alone is not in the current list. All listing text and starter
  prompts meet the final submission limits, not merely upload limits.
- `assets/icon.png` is an original book-and-spark PNG, used for `logo` and
  `composerIcon`. Its opaque background works in either theme. Separate dark
  variants are optional. PNG, JPEG, WebP and SVG are currently accepted, up to
  5 MiB per icon; icons must be square, at least 48×48, with raster dimensions
  no larger than 4096×4096. No screenshots are included: this plugin has no
  custom MCP UI.
- [PRIVACY.md](../PRIVACY.md) describes the package's own data practices;
  [SUPPORT.md](../SUPPORT.md) points to GitHub Issues. Neither file claims
  control over the host's data retention.

Version remains **1.2.0** for this additive packaging change: this is the first
portable public-submission package, preserving the existing release identity
and subject content. Future published package updates need a new version in
both manifests; validation rejects drift.

## Validate and build locally

Maintainer tooling requires Python **3.9+** and three declared development
libraries. Tutoring users, including mobile users, do not install these.

```sh
python3 -m venv .venv
```

Use `.venv/bin/python` on macOS/Linux or `.venv\Scripts\python.exe` on Windows
in place of `python3` for the following commands when using the virtual
environment:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests -v
python3 scripts/build_openai_plugin.py
```

Run from the repository root. The build output is:

```text
dist/gsat-tutor-openai-1.2.0.zip
└── gsat-tutor/
    ├── plugin.json
    ├── assets/icon.png
    ├── skills/                       # all five skills, references, PDFs, helper
    ├── README.md
    ├── PRIVACY.md
    ├── SUPPORT.md
    └── LICENSE
```

The upload accepts a single top-level plugin directory. Build uses an explicit
allowlist and a temporary staging directory, fixes ordering, timestamps and
permissions, and validates the extracted ZIP. Rebuilds are byte-identical with
the same sources and Python/zlib versions. The ZIP stays below the documented
100 MB compressed limit. `.git`, caches, editor files, maintainer tooling,
tests, eval output, and local marketplace/manifests are excluded. `dist/` is
ignored; do not commit generated ZIPs.

Validation uses an unmodified, vendored official JSON Schema, retrieved on
2026-10-07, so checks work offline. The schema deliberately leaves extension
semantics to clients; the validator additionally checks OpenAI's documented
listing limits and this project's compatibility/runtime requirements. It is
not OpenAI's security scan. The installed Codex CLI exposes no standalone
official plugin validation command; the portal performs authoritative checks.

## What the owner must do in the dashboard

1. Run the commands above and inspect the ZIP. Confirm redistribution rights
   and retain attribution for the bundled CEEC PDFs and vocabulary transcript;
   these resources retain their existing non-commercial notices and are
   excluded from the project's GPL grant. Choose the release's country
   availability; it is intentionally not inferred from the subject or publisher.
2. **Recheck the published privacy page.**
   [PRIVACY.md on GitHub](https://github.com/Samson-Ho/GSAT-Tutor/blob/main/PRIVACY.md)
   was published and verified without authentication on 2026-10-07. Its URL is
   included as `extensions.com.openai.interface.privacyPolicyURL`. Confirm the
   page still serves the current policy before each submission; if you move it,
   verify the replacement HTTPS URL and rebuild the package.
3. Open the [Plugin submission portal](https://platform.openai.com/plugins).
   Select the intended organization/project. An organization owner can submit;
   other members need **Apps Management Write**. Complete individual identity
   verification for **Samson Ho**, or the authorized business identity if
   publishing under a different name. The verified identity controls the public
   developer name; package text cannot override it.
4. Select **Upload new or existing plugin**, choose the verified developer
   identity, and upload the ZIP. If the portal presents **Create plugin →
   Skills only**, select that equivalent path. There is no MCP setup, OAuth,
   server/domain verification, demo recording, or MCP test-case requirement for
   this package.
5. Inspect **Metadata & Skills** for the uploaded version. Check all five
   skills, imported text, category, starter prompts, logo, URLs, release notes,
   developer identity, and intended country availability. A portable upload may
   generate internal Codex compatibility files; do not copy those bindings back
   into the source ZIP as extra app references.
6. Wait for all metadata and skill safety/security checks; skills scans can take
   up to two hours. Read findings, correct the source, rebuild, and use **Upload
   plugin to fix issues**. Confirm the new version's checks. Do not treat local
   validation as a passed portal scan.
7. Complete the dashboard's required policy/legal attestations yourself.
   Skills-only ZIP validation makes listing URLs optional, but the general
   plugin guidelines require a published privacy policy. Confirm its live link
   and publisher identity. If the dashboard requires additional policy or terms
   pages, publish appropriate pages and populate the actual verified URLs; do
   not use a software LICENSE as invented service terms. Keep country choices
   and any commerce answers accurate; this code has no purchase/payment flow.
8. Test the imported skills in a clean host environment with the three starter
   prompts and `evals/evals.json`, plus 國綜 and 國寫 requests. Check scope,
   scoring, source access, and the no-shell fallback. Do not assert mobile tests
   succeeded unless run on those clients.
9. Submit the selected draft for review. Resolve requests from reviewers.
10. After approval, open the approved version and select **Publish plugin**.
    Approval and publication are separate steps.
11. Verify the published listing in the universal directory. Install from
    **Plugins**, search **GSAT-Tutor**, and test independently on ChatGPT Web,
    iPhone, iPad, desktop, and Codex where available. Web/mobile users should
    not clone GitHub or add the Claude marketplace. Also smoke-test the existing
    local marketplace and Claude Code paths. Record actual client/account
    availability and results before advertising mobile availability.

Pushing source, building a ZIP, uploading a draft, and passing automated checks
do not by themselves complete directory publication. Identity verification,
 owner attestations, portal scans, review approval, publication,
and client smoke tests remain external steps.

## Official references checked on 2026-10-07

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Upload and submit](https://developers.openai.com/plugins/deploy/submission)
- [Convert a Claude Code plugin](https://developers.openai.com/plugins/guides/submit-claude-plugin)
- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines)
- [Submission errors and final limits](https://developers.openai.com/plugins/deploy/submission-errors)
- [Build skills](https://developers.openai.com/plugins/build/skills)
- [Agent Plugins JSON Schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)

Recheck these before each submission; if the portal differs, use its current
requirements and update this guide.
