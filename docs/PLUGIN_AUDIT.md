# Portable-package audit

Audit date: 2026-10-07. Source: repository HEAD
`1963dc65520a9c81c254e837690b6b9f3b0dc318`, matching remote HEAD when checked.
The working tree was clean before this migration.

## Inventory and findings

| Skill | Reference Markdown files | PDF assets | Runtime code |
|---|---:|---:|---|
| `gsat-math-a` | 5 | 8 | None |
| `gsat-science` | 5 | 9 | None |
| `gsat-english` | 6 | 9 | Optional `scripts/vocab_level.py` |
| `gsat-chinese` | 5 | 8 | None |
| `gsat-chinese-writing` | 5 | 7 | None |

All subjects retain their scope, trends, question index, item-writing and
grading references. English retains the complete 6,012-entry vocabulary
transcript. All 41 PDF assets and the vocabulary helper remain unchanged.
`evals/evals.json` contains seven behavioral evaluation definitions, with no
checked-in executable runner.

- **YAML:** all five original descriptions were unquoted strings containing
  `: ` and failed a real YAML parser. They are now quoted without changing
  their text. Names match folders; descriptions range from 669 to 891
  characters, within the 1,024-character limit. Combined plugin/skill
  identities fit within 64 characters.
- **Runtime assumptions:** all five skills formerly prescribed local PDF
  extraction/rendering tools. English additionally prescribed grep and a
  Python script. A common portability section now makes host resource reading
  and text references the core path. Local Python, pypdf, pypdfium2/Pillow,
  Poppler and Ghostscript are optional existing tools, with no install step
  required from students. Missing exact figures/rubrics trigger a request for
  source material and clearly labelled provisional guidance.
- **Provider neutrality:** shared skills already contained no Claude/ChatGPT/
  Codex-specific artifact APIs, settings, personas or installation hooks.
  No provider-name replacement was needed. Host-neutral resource search
  replaces mandatory grep/script use in English's instructions and
  `references/item-writing.md`.
- **Paths and dependencies:** package-relative references resolve successfully.
  The unchanged vocabulary helper locates its data relative to `__file__` and
  imports only Python standard-library modules. It works from another working
  directory. No hard-coded developer paths, local Git dependencies, localhost,
  Homebrew, MCP, backend, database, OAuth, telemetry, credentials, or external
  runtime service are required. CEEC is a source/attribution link, not a
  required runtime API.
- **Other components:** no commands/agents tree, hooks, `CLAUDE.md`,
  `userConfig`, `${user_config.*}`, executable installation prompts, or live
  artifact dependency was present. There are no hidden app/server bindings to
  migrate.
- **Metadata:** both Claude JSON files were valid. Root identity metadata now
  matches the Claude manifest; version remains 1.2.0. The existing catalog is
  deliberately byte-for-byte unchanged, including its historical shorter
  two-subject description. The package still contains all five skills.
- **Security scope:** the upload allowlist, text checks for developer paths and
  obvious credential patterns, symlink rejection, icon decoding, PDF header
  checks, and extracted-ZIP checks pass. These are packaging checks, not a
  malware analysis or the portal's security/safety scan.
- **Public URLs:** repository homepage and GitHub Issues were fetched without
  authentication and identified this project. `PRIVACY.md` is new local source;
  its public page has not been published/verified, so `privacyPolicyURL` is
  absent until the owner completes the documented publishing step. No terms
  URL or country availability was invented.
- **Copyright:** existing CEEC attribution, non-commercial notices and GPL
  exclusions are preserved. The owner must confirm rights for public
  distribution when making the portal's attestations; this audit does not
  confer or certify those rights.

## Packaging and verification

The canonical OpenAI manifest is root `plugin.json`, using Agent Plugins
1.0.0 and inline `extensions.com.openai`. No Codex fallback or duplicate
marketplace is added. Claude files remain in the repository but are not needed
in the portable public archive. The root manifest discovers shared `skills/`
automatically. Current official requirements and remaining owner steps are
linked in [OPENAI_SUBMISSION.md](OPENAI_SUBMISSION.md).

The vendored, unmodified official schema has SHA-256:

```text
0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883
```

Validation and all 17 regression tests pass on Python 3.9. Tests cover valid
source, real YAML parsing, invalid JSON/nonzero exit, schema-invalid fields,
version drift, missing skills/PDFs, escaping references, final listing limits,
category and prompts, credential URLs, corrupt/missing icons, accidental
secrets without echoing values, absolute machine paths, symlinks, marketplace
source/duplicates, forbidden app/MCP configuration, deterministic ZIP contents,
and the existing vocabulary helper from another working directory.

The generated ZIP has one top-level `gsat-tutor/` directory and 79 files: all
five skills, 26 references, 41 PDFs, the optional vocabulary script, icon and
distribution documents. It excludes marketplace/compatibility files, Git data,
caches, development dependencies, tests and eval output. It is approximately
66.1 MB compressed, below the 100 MB limit. The extracted package also passes
validation. Repeated builds with unchanged source and the same Python/zlib
produce the same SHA-256.

Seven existing tutoring eval definitions were inspected and retained; live
model behavioral evaluation on Claude/ChatGPT and web/iPhone/iPad installation
have **not** been run. They remain host smoke tests, not claims of passed
automated pedagogical evals. The installed Codex 0.160.0 CLI provides no
standalone official plugin-validation command. No submission, review approval,
public listing, or mobile availability has been verified.

## Original icon

`assets/icon.png`: PNG, RGB, 1254×1254 pixels, 1,235,654 bytes. It is used for
both the listing logo and composer icon, with no borrowed organizational
branding or endorsement. Opaque blue backing preserves contrast in light and
dark hosts. Optional dark variants and screenshots are omitted.

Generated using the built-in image-generation tool. Final generation prompt:

> Use case: logo-brand. Asset type: square PNG app icon for GSAT-Tutor, an independent Taiwan high-school exam tutoring plugin. Create a polished minimal original mark: an open white book with five subtle page divisions and a small golden spark above it, centered on a solid deep blue background. Flat vector-like graphic, bold simple shapes, generous margins, highly legible at 48 pixels, no gradients, no small details. Square 1024 by 1024 composition, opaque background. No text, no letters, no CEEC, OpenAI, Anthropic, government or university logos; no watermark. This is a final standalone icon, not a mockup or icon sheet.

The tool returned a 1254×1254 PNG, which meets the current size requirements;
the actual file, not the requested dimensions, is validated.
