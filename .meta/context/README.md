# Maintaining this profile

## Purpose and authority

Introduce Pradeep, his approach, and useful work to engineers, recruiters, fellow
builders, and curious visitors. The README owns content; this guide records upkeep.
His current request and revisions override guidance and older commits. Distinguish
reviews from edits; honor the requested commit/push boundary and final wording.
A supplied resume can inform understanding without being copied or published.
Leave pins and personal uploads to Pradeep unless requested.

## Identity and voice

Preserve the current title, entire automation poem, and final `[EOF]:` definition
byte-for-byte against the starting working copy unless Pradeep authorizes changes.
Keep EOF last with its existing separation. Do not duplicate protected content
here or restore older versions over his revisions. Use simple, direct, first-person
speech: professional, curious, and occasionally dry or absurd. Avoid cheesy slogans,
hype, jargon, generic prose, and repetition. Preserve personal quirks; Thoughts can
be more critical and playful. No waving-hand emoji in headers.

## Presentation and rendering

Keep the Python class/method/attribute theme as readable pseudocode. Methods go
under classes; their content uses attributes and calls such as
`self.identity.group("Core")`, not nested function headings. Use Title Case human
group labels and meaningful, restrained parameters. Preserve current ordering
and disclosure defaults; the README owns their exact names and settings.
Bold and underline group-name words inside summaries, excluding quotes and call
syntax. Use `<ins>` for underlining; GitHub's renderer strips `<u>`.
Values and practices use a concise bold lead-in without a trailing period,
followed by an em dash and a plain-language explanation.

Keep the welcome centered and identity onward left-aligned. Standalone badges go
beneath the class header, separated by spaces; links follow, separated by dots.
Author, sections, and the comment share one centered Python fence with blank lines.
Keep badges selective and use icons where available. Badge images inside
`<pre><code>` failed on the live GitHub profile despite passing local/API previews.

Keep class and method headings visible, with emojis before their names. The outer
dropdown experiment is retained in Git history; do not restore it unless requested.
Use inline native dropdowns for grouped content. Values opens Intentions and closes
Practices; Tech Stack opens Software & Platforms and closes its other groups.
Preserve other defaults. Show useful content immediately and let secondary groups
invite exploration. Heading-sized summaries can detach arrows in VS Code.
Use one `<br/>` between main sections; do not stack breaks outside the EOF ending.
Use `<p></p>` between inner groups and after inline summaries;
avoid stacked spacers. Put fragment anchors inside headings to avoid empty-paragraph margins.
Keep adjacent closing `</details>` tags on consecutive lines, retain blank lines
around Markdown blocks, and preserve the deliberate three-break EOF separation.
Avoid blockquote indentation, CSS/JavaScript, and nonworking open-all
controls. Long identity and thought prose uses blockquotes with inline code variable
labels; explanatory notes can use an inline `#` label. Keep each assignment or
sentence on one source line and let prose wrap naturally. Reserve code blocks for
the poem, lists, and short code; do not force prose wrapping with triple-quoted
strings or manual line breaks. Indent multiline lists and pad inline lists inside
brackets. Preserve the detailed grouped tech stack, inline code,
major-tool markers, and legend; do not condense it unless asked.

## Project truth and metadata

Keep established cloud, DevOps, and platform work visible alongside AI exploration.
Use concise purposes and the README's Flow, Maturity, Status, Activity, and Tags
format and definitions. Each project is an inline `<details>` entry whose summary
holds the linked title and purpose, followed by a two-column, five-row metadata
table with blank column headings; `self.projects.info()` shows that layout as one
bullet. Keep entries contiguous inside each group's `<dl><dd>` wrapper.
Education, certification, and study repositories belong under Learning. Intended flow differs from implemented behavior. Releases,
recent commits, and passing checks do not prove readiness, maintenance, or value;
pre-v1 releases are displayed as `Experimental` with their verified version.
Do not invent claims or outcomes.
Verify public identities, URLs, and capabilities against public source. Private
or proposed work can appear at Pradeep's approved level, labeled without dead
links or private details. Deep AI is a unified ambition until demonstrated;
provider projects should remain independently useful. Keep future Maestro distinct
from the old URL redirecting to Signals. Separate actual practice from planned
exercises and credit upstream work; a fork does not establish authorship.

### Software readiness

The README `self.projects.info()` table owns the maturity convention: `Idea`
for a concept or planned collection; `Experimental` for an evolving
implementation or existing collection. Pre-v1 releases retain their verified
version beside `Experimental`; a version alone requires a verified v1.0.0+
release. Do not invent tags or add maturity synonyms. Private is visibility,
not maturity. Status describes what a collection contains and its study,
reference, or practice purpose; these collections carry no software TRL or
credential claim.

The README legend owns the TRL definition. ` · TRL N` is appended only for
projects meant to become shared, useful products. Idea often corresponds to
1–2 and Experimental to 3–5; these are rough associations, not conversion
rules. Keep the evidence-based TRL independent of maturity and release version.
It is Pradeep's conservative self-assessment of the technical behavior in the intended flow, adapted from
[Wikipedia](https://en.wikipedia.org/wiki/Technology_readiness_level) and
[NASA ESTO software TRLs](https://esto.nasa.gov/trl/). It is not certification.
Versions, test counts, popularity, and demand do not raise a level; usefulness
and human value are judged separately. Raise a level only with retained evidence
that the next stage's integration or environment was actually exercised.
For already approved private descriptions, mark an unverified rating provisional
and publish no private implementation evidence or links.

Assessed 2026-10-14 from public READMEs, pinned docs, selected integration-test
source, head commits, and releases. Existing acceptance records inform the
ratings; the product test suites were not rerun or fully audited here. A low
fidelity integrated workflow can support 4 without proving usefulness. Moving
to 5 needs relevant-environment performance and scaling evidence; missing
human-value measurements alone do not cap technical readiness.

- **Signals AI** `TRL 3` ([`1d6cfb6`](https://github.com/pradeeptathineni/signals-ai/tree/1d6cfb6fbe355256b912a2ed042547dd3cf04ff5), `v0.3.0`) — Research, claim checks, retention, and the public Corpus exist, with controlled integration checks. For the broader evidence-assessment flow, live research quality and source-scoped semantic accuracy lack established validation against defined acceptance criteria. That critical behavior keeps this scope at 3; individual deterministic components can be further along. Human decision benefit is a separate unknown.
- **Context AI** `TRL 4` ([`aab3872`](https://github.com/pradeeptathineni/context-ai/tree/aab3872d9a34c54d5172403f48978edc5c4b6915), `v0.3.0`) — The [acceptance record](https://github.com/pradeeptathineni/context-ai/blob/aab3872d9a34c54d5172403f48978edc5c4b6915/evals/v1-acceptance.md) documents disposable-consumer plan/apply/reapply/verify/undo and conflict protection. [Consumer-path checks](https://github.com/pradeeptathineni/context-ai/blob/aab3872d9a34c54d5172403f48978edc5c4b6915/tests/test_consumer_path.py) exercise explanation, selection, installation, and verification boundaries together. This supports controlled integration of reusable guidance delivery. Not 5: relevant-workload performance and scaling are not established. Installation integrity and improved agent work remain separate observations.
- **Blueprint AI** `TRL 4` ([`8965edb`](https://github.com/pradeeptathineni/blueprint-ai/tree/8965edb5eabb2688db66e461e8c1ba314dfbcfd2), `0.9.0`) — The [published transformation evidence](https://github.com/pradeeptathineni/blueprint-ai/blob/8965edb5eabb2688db66e461e8c1ba314dfbcfd2/docs/phase-7-evidence.json) records native preview/apply, repeatability, verification, and exact rollback on supported cases, plus a scoped workflow-only change in an upstream checkout. This supports controlled integration of the CLI workflow. It does not validate every advertised project family, complete model review, or relevant-environment performance and scaling for 5.
- **ShouldaUsedThat** `TRL 4` ([`6edaff0`](https://github.com/pradeeptathineni/shoulda-used-that/tree/6edaff07d582a2d2d2d06145643f22dbfee3ca0e), `v0.4.0`) — The deterministic CLI, retained decisions, and reviewed catalog form an integrated workflow. The [CLI chain](https://github.com/pradeeptathineni/shoulda-used-that/blob/6edaff07d582a2d2d2d06145643f22dbfee3ca0e/tests/test_cli.py) checks candidate selection, recording a decision, and rechecking retained state with controlled fixtures. The [product contract](https://github.com/pradeeptathineni/shoulda-used-that/blob/6edaff07d582a2d2d2d06145643f22dbfee3ca0e/docs/architecture/product-contract.md) reserves contextual assessment for reviewed inputs. This is a bounded technical rating; judgment is an intended part of the flow. Realistic decision-brief performance and scaling are not validated for 5, and saved decisions do not establish better decisions.
- **AWS CLI Plus** `TRL 3` ([`c90f092`](https://github.com/neon1llc/aws-clip/tree/c90f092292cd2dd60be89ea906777c667666b4c5)) — The wrapper implements identity checks, policy, and guarded commands. [Workflow test source](https://github.com/neon1llc/aws-clip/blob/c90f092292cd2dd60be89ea906777c667666b4c5/internal/cli/workflow_test.go) exercises planning and fake-AWS execution, but the collected record does not establish an observed integrated account/authentication validation. Keep 3 until that evidence is retained; no live AWS account was queried for this assessment.
- **Intentional AI** `TRL 2`, provisional — The approved description formulates scheduled, bounded project work and mentions private experiments. Those experiments were not re-reviewed here; their technical readiness remains unverified beyond the described concept. Publish no private implementation evidence.
- **Maestro AI** and **Deep AI** `TRL 2` — Concepts are formulated; nothing is implemented.

Collection maturity follows the same small vocabulary. AWS IaC Terraform and
Johns Hopkins use `Idea` because no templates or coursework projects exist yet.
Planning, Principles, Sandbox, Labs, Home Lab, Nature of Code, System,
UT Austin, the upstream AI Engineering from Scratch fork, and the Terraform
challenge use `Experimental` because material or implementations exist.
Their existing Status fields distinguish notes, guidance, methods, practice,
configuration, coursework, and upstream authorship; no collection gets a TRL.
Learning entries link no solutions and claim no completed program or credential.

Sandbox remains documents and trial records at
[`a252e4f`](https://github.com/pradeeptathineni/sandbox-ai/tree/a252e4f9d8f9592130502ca13c84f7e91c3e52a8).
Its Watchexec report records bounded execution on synthetic inputs, not product
validation. It supplies no runner. Keep Sandbox immediately below Signals.
The Deep AI comment describes intended discovery → Sandbox testing → potential
Context adoption. Trial results inform a reviewed adoption choice; this is
not an implemented automatic cross-project integration.

The public owner inventory has 16 repositories. Fifteen have entries, plus AWS
CLI Plus under neon1; the profile repository is this README. Activity uses each
default-branch head commit converted to New York time; a fork's date can
reflect upstream commits.

Use `python3 .meta/scripts/project_metadata.py` for public release/activity facts.
It reads GitHub through authenticated `gh`, uses New York dates, and does not
rewrite the README. Private queries require explicit `--include-private` opt-in.
Refresh the public check date with the facts. Human review owns purpose, current
status, and usefulness; the script cannot infer them from repository metadata.
Its `maturity` and `preview` fields are observed release facts, not extra display
categories. Apply the README convention manually when updating maturity cells.

## Media and collaboration

Use optional collapsed `self.imagine(variable)` image companions that fit their
thoughts. Center images with compact `<sup><em>` credits in the same paragraph,
separated by one `<br/>`. Preserve supplied artwork, alt text, terms, and required
notices; [assets/README.md](../../assets/README.md) owns detailed credits. Credit
grants no rights. The favorite meme stays optional and before EOF. Keep disclaimers
compact. AI can assist research, planning, implementation, and review; Pradeep owns
decisions, verification, and results. No apologetic authorship badges.

## Maintenance and checks

Inspect Git status and remote state; use fast-forward-only pulls and preserve
local work. Verify protected content, relevant links, assets, attribution,
disclosure defaults, and `git diff --check`. For layout changes, inspect VS Code
behavior and the actual GitHub UI when available, including loaded images and
working links. An API/local preview is not live validation; never publish solely
to test without authority. State what was actually checked.
After README edits, review as a hurried visitor, fellow engineer, and author;
reread guidance and make a deliberate second pass without gratuitous edits.
For context-only work, verify the profile and assets remain untouched. Update
this guide for observed gaps and keep it concise. No duplicate policy or framework
and no Context AI runtime dependency; useful patterns may later inform Context AI
without implying automatic synchronization or universal ownership.
