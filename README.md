<h1 align="center">⭐ class Deep(Github):</h1>

<p align="center">
  <a href="#tech-stack"><img src="https://img.shields.io/badge/macOS-64748B?logo=macos&amp;logoColor=white&amp;style=flat" alt="macOS"></a>
  <a href="#tech-stack"><img src="assets/badges/vscode.svg" alt="VS Code"></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&amp;logoColor=white&amp;style=flat" alt="Python, my primary language"></a>
  <a href="#tech-stack"><img src="assets/badges/aws.svg" alt="AWS"></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&amp;logoColor=white&amp;style=flat" alt="Docker"></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Terraform-7B42AC?logo=terraform&amp;logoColor=white&amp;style=flat" alt="Terraform"></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&amp;logoColor=white&amp;style=flat" alt="GitHub Actions"></a>
  <a href="#tech-stack"><img src="assets/badges/codex.svg" alt="Codex, one of my primary AI tools"></a>
  <a href="#tech-stack"><img src="assets/badges/chatgpt.svg" alt="ChatGPT, one of my primary AI tools"></a>
</p>

<p align="center"><strong>
  <a href="#projects">Projects</a> ·
  <a href="https://pradeeptathineni.github.io/labs/">Labs</a> ·
  <a href="https://github.com/pradeeptathineni?tab=stars">GitHub Stars</a> ·
  <a href="https://github.com/neon1llc">neon1</a> ·
  <a href="https://www.linkedin.com/in/pradeep-tathineni/">LinkedIn</a>
</strong></p>

<div align="center">

```python
self.AUTHOR = "Pradeep Tathineni" if env.PROPER else "Deep"

self.SECTIONS = [ self.identity, self.values, self.projects, self.tech_stack, self.neon1, Meta ]

# Could you imagine if we chose to center our code?
```

</div>
<br/>

## 🪪 def identity(self, title="Hello World!"):

<details open>
<summary>self.identity.group(<strong>"<ins>Core</ins>"</strong>)</summary>

<p></p>

`self.WHO` = "I'm an engineer who sees repeated work as a design problem: if I have to do it twice, I start asking why the computer isn't doing it."

```python
# Once is flirtation. Twice is frustration.
# Once is temptation. Twice is libation.
# Once is foundation. Twice is causation.
#
# All thereafter is automation.
```

`self.WHAT` = "I have 8+ years of professional experience in automation, application development, cloud, DevOps, and security, and nearly two decades of exploring technology."

`self.WHY` = "I build technology to make people's work and lives easier."

</details>

<p></p>

<details>
<summary>self.identity.group(<strong>"<ins>More</ins>"</strong>)</summary>

<p></p>

```python
self.FOCUSES["domains"] = [
    "Automation", # performance
    "Cloud",      # enablement
    "DevOps",     # delivery
    "Security",   # confidence
    "AI",         # automation 2.0
]

self.FOCUSES["concepts"] = [
    "Open Source",
    "Prior Art",
    "Developer Tools",
    "Evidence-Based Decisions",
]

self.FOCUSES["exploring"] = [
    "Simulation",
    "Computer Vision",
    "EdTech",
    "EnviroTech",
    "AgriTech",
    "GeoTech",
]

self.INTERESTS = [
    "Dog", # TODO Add link to dog pic
    "Education",
    "Community",
    "Gardening",
    "Biking",
    "Hiking",
    "Tacos",
    "Driving Fast",
]
```

</details>

<br/>

## 🧭 def values(self, group="technology"):

<details open>
<summary>self.values.group(<strong>"<ins>Intentions</ins>"</strong>)</summary>

<p></p>

`#` **Make technology useful** — Help people get things done, whether that means a small tool, a better application, or infrastructure they can depend on.\
`#` **Automate with care** — Take repeated work off people's hands and build systems that are dependable, understandable, and easy to change.\
`#` **Keep learning and share** — Explore unfamiliar problems, question what I think I know, and share what I learn.\
`#` **Build with open source** — Learn from existing work, adapt what fits, and contribute tools that others can use. Start with a real need.\
`#` **Advance my engineering practice through AI** — Bring the same care to AI-assisted research, planning, and development: give it useful context, coordinate the work, and check the results.

</details>

<p></p>

<details>
<summary>self.values.group(<strong>"<ins>Practices</ins>"</strong>)</summary>

<p></p>

`#` **Research deeply before building** — Compare existing tools and approaches. My [GitHub Stars](https://github.com/pradeeptathineni?tab=stars) collect possibilities to investigate.\
`#` **Back claims with evidence** — Cite sources, measure results, and compare them with a baseline.\
`#` **Generalize across real use cases** — Try an idea against different needs before turning it into a shared solution. Keep the differences that matter.\
`#` **Remove, automate, verify, and revisit** — Keep changes small, check that they help, and keep a way to recover.

</details>

<br/>

## <a name="projects"></a>🚀 def projects(self, type="personal"):

<details>
<summary>self.projects.info()</summary>

<p></p>

- Project Name/Link — Short project description.
  | | |
  | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Flow** | The intended path from input → outcome. |
  | **Maturity** | · `Idea`: concept only; `Experimental`: evolving implementation, including pre-`v1.0.0` releases.<br/>· Keep a verified pre-v1 version beside `Experimental`; use a verified `v1.0.0`+ release version on its own.<br/>· For study, practice, and reference collections, `Idea` means planned content and `Experimental` means material exists, without a software-readiness or credential claim.<br/>· Intended shared products append ` · TRL N` independently; collections have no TRL. |
  | **Status** | What exists and works today. |
  | **Activity** | · Updated: last default-branch commit date.<br/>· `Recent` means within 30 days of the refresh, otherwise `Quiet`.<br/>· Proposed projects show planning status instead. |
  | **Tags** | Technologies and areas of focus. |

`#` **Software TRL** — `2` concept formulated · `3` critical-function proof of concept · `4` integrated and validated in a controlled setting · `5` end-to-end validation in a relevant setting.\
`#` `Idea` often corresponds to TRL 1–2 and `Experimental` to TRL 3–5; these are not conversion rules, and a release version does not establish a level.\
`#` Adapted from [Wikipedia](https://en.wikipedia.org/wiki/Technology_readiness_level) and [NASA ESTO's software TRLs](https://esto.nasa.gov/trl/). It rates technical readiness, not usefulness or demand, and is not a certification.

</details>

<p></p>

<!-- Refresh facts: python3 .meta/scripts/project_metadata.py; use --include-private OWNER/REPO for each private project and --write to reconcile activity rows. -->

<details>
<summary>self.projects.group(<strong>"<ins>Cloud and DevOps Engineering</ins>"</strong>)</summary>

<p></p>

<dl><dd>

<details data-repo="pradeeptathineni/eng-challenge-aws-terraform">
<summary><a href="https://github.com/pradeeptathineni/eng-challenge-aws-terraform"><strong>AWS Terraform Engineering Challenge</strong></a> — Make AWS web infrastructure reproducible and inspectable.</summary>

|              |                                                                                                   |
| :----------- | :------------------------------------------------------------------------------------------------ |
| **Flow**     | _requirements → Terraform plan → deploy → verify → tear down_                                     |
| **Maturity** | `Experimental`                                                                                         |
| **Status**   | Modular infrastructure, CI, and deployment checks exist. This is still a challenge-scale project. |
| **Activity** | Updated 2026-09-12 · `Quiet`                                                                      |
| **Tags**     | `aws` ; `terraform` ; `devops`                                                                    |

</details>

<details data-repo="pradeeptathineni/aws-iac-terraform">
<summary><a href="https://github.com/pradeeptathineni/aws-iac-terraform"><strong>AWS IaC Terraform</strong></a> — Reserve a home for reusable AWS infrastructure templates.</summary>

|              |                                                                  |
| :----------- | :--------------------------------------------------------------- |
| **Flow**     | _need → template → plan → apply → reuse_                         |
| **Maturity** | `Idea`                                                           |
| **Status**   | README-only scaffold. No templates or modules are published yet. |
| **Activity** | Updated 2025-07-13 · `Quiet`                                     |
| **Tags**     | `aws` ; `terraform` ; `iac`                                      |

</details>

</dd></dl>

</details>

<p></p>

<details>
<summary>self.projects.group(<strong>"<ins>Automation and Tooling</ins>"</strong>)</summary>

<p></p>

<dl><dd>

<details data-repo="neon1llc/aws-clip">
<summary><a href="https://github.com/neon1llc/aws-clip"><strong>AWS CLI Plus</strong></a> — Make multi-profile AWS CLI work easier to follow and safer.</summary>

|              |                                                                                            |
| :----------- | :----------------------------------------------------------------------------------------- |
| **Flow**     | _select profile → verify identity → check policy → run AWS CLI_                            |
| **Maturity** | `Experimental` · TRL 3                                                                     |
| **Status**   | Working Go wrapper around AWS CLI v2. Account checks and guarded commands are implemented. |
| **Activity** | Updated 2026-09-13 · `Quiet`                                                               |
| **Tags**     | `aws` ; `cli` ; `go` ; `automation`                                                        |

</details>

<details data-repo="pradeeptathineni/shoulda-used-that">
<summary><a href="https://github.com/pradeeptathineni/shoulda-used-that"><strong>ShouldaUsedThat</strong></a> — Find what to reuse, what to skip, and what remains worth building.</summary>

|              |                                                                                                                                                                      |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _problem → candidates → evidence → decision → revisit_                                                                                                               |
| **Maturity** | `Experimental` · [`v0.4.0`](https://github.com/pradeeptathineni/shoulda-used-that/releases/tag/v0.4.0) · TRL 4                                                       |
| **Status**   | Deterministic CLI and [reviewed catalog](https://pradeeptathineni.github.io/shoulda-used-that/curation/) exist. Each reuse decision still needs contextual judgment. |
| **Activity** | Updated 2026-10-22 · `Recent`                                                                                                                                        |
| **Tags**     | `oss` ; `prior-art` ; `python`                                                                                                                                       |

</details>

<details data-repo="pradeeptathineni/system">
<summary><a href="https://github.com/pradeeptathineni/system"><strong>System</strong></a> — Keep my shell configuration in version control.</summary>

|              |                                                                 |
| :----------- | :-------------------------------------------------------------- |
| **Flow**     | _open shell → load configuration → work_                        |
| **Maturity** | `Experimental`                                                  |
| **Status**   | One public `.bashrc` file. No README or broader system tooling. |
| **Activity** | Updated 2025-07-13 · `Quiet`                                    |
| **Tags**     | `bash` ; `shell` ; `dotfiles`                                   |

</details>

</dd></dl>

</details>

<p></p>

<details>
<summary>self.projects.group(<strong>"<ins>AI Systems</ins>"</strong>)</summary>

<p></p>

`#` I'm exploring how AI can help me research, plan, build, and coordinate engineering work.

<dl><dd>

<details data-repo="pradeeptathineni/research-ai">
<summary><a href="https://github.com/pradeeptathineni/research-ai"><strong>Research AI</strong></a> — Investigate questions with clear limits and traceable sources.</summary>

|              |                                                                  |
| :----------- | :--------------------------------------------------------------- |
| **Flow**     | _question → retained sources → investigation → qualified findings_ |
| **Maturity** | `Experimental` · TRL 4 |
| **Status**   | Native research sessions can examine support for claims and explore perspectives from sources. Model judgments remain fallible. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `research` ; `evidence` ; `javascript` |

</details>

<details data-repo="pradeeptathineni/principles-ai">
<summary><a href="https://github.com/pradeeptathineni/principles-ai"><strong>Principles AI</strong></a> — Research and record domain principles I can understand, apply, and revisit.</summary>

|              |                                                                                                 |
| :----------- | :---------------------------------------------------------------------------------------------- |
| **Flow**     | _research → reconcile → define → apply → reassess_                                              |
| **Maturity** | `Experimental`                                                                                  |
| **Status**   | Structured corpus and validation tooling exist. The guidance remains under research and review. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `principles` ; `learning` ; `evidence`                                                   |

</details>

<details data-repo="pradeeptathineni/signals-ai">
<summary><a href="https://github.com/pradeeptathineni/signals-ai"><strong>Signals AI</strong></a> — Find research worth keeping and revisit it when a decision needs it.</summary>

|              |                                                                                                                                                       |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _finding → assess → compare → retain → revisit_ |
| **Maturity** | `Experimental` · [`v0.3.0`](https://github.com/pradeeptathineni/signals-ai/releases/tag/v0.3.0) · TRL 3                                               |
| **Status**   | Library search, discussions over saved answers and optional check suggestions work. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `discovery` ; `evidence` ; `typescript` |

</details>

<details data-repo="pradeeptathineni/sandbox-ai">
<summary><a href="https://github.com/pradeeptathineni/sandbox-ai"><strong>Sandbox AI</strong></a> — Plan limited trials, compare options, and record what the evidence supports.</summary>

|              |                                                                                                                           |
| :----------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Flow**     | _candidate → bounded trial → record evidence → review → advisory decision_                                                |
| **Maturity** | `Experimental` · TRL 3                                                                                                    |
| **Status**   | Trial plans can be frozen and attempts sealed, with a working recipe for testing Context. The host runs trials; comparisons alone do not prove usefulness. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `evaluation` ; `evidence` ; `methods`                                                                              |

</details>

<details data-repo="pradeeptathineni/custom-ai">
<summary>🔒 <strong>Custom AI</strong> — Keep personal preferences and writing examples under my control.</summary>

|              |                                                                  |
| :----------- | :--------------------------------------------------------------- |
| **Flow**     | _permissioned examples → task context → revision → preference decision_ |
| **Maturity** | `Experimental` · Private · TRL 4 |
| **Status**   | Private writing kits support revision feedback, explicit preference decisions and undo. Example selection matches words and tags; claim checks use heuristics. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `writing` ; `preferences` ; `python` |

</details>

<details data-repo="pradeeptathineni/context-ai">
<summary><a href="https://github.com/pradeeptathineni/context-ai"><strong>Context AI</strong></a> — Supply relevant engineering guidance for the task at hand.</summary>

|              |                                                                                                         |
| :----------- | :------------------------------------------------------------------------------------------------------ |
| **Flow**     | _task → select guidance → preview → apply → verify → undo_ |
| **Maturity** | `Experimental` · [`v0.3.0`](https://github.com/pradeeptathineni/context-ai/releases/tag/v0.3.0) · TRL 4 |
| **Status**   | Task-scoped guidance, provenance, private loadouts and reversible installation work; everyday usefulness remains under evaluation. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `context-engineering` ; `devtools` |

</details>

<details data-repo="pradeeptathineni/planning-ai">
<summary>🔒 <strong>Planning AI</strong> — Turn goals and evidence into plans I can review and revise.</summary>

|              |                                                                  |
| :----------- | :--------------------------------------------------------------- |
| **Flow**     | _evidence → goal → recipe or tasks → preview → approve_ |
| **Maturity** | `Experimental` · Private · TRL 4 |
| **Status**   | Evidence-linked plans, typed recipes and ordered tasks feed reviewed Maestro execution. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `planning` ; `evidence` ; `python` |

</details>

<details data-repo="pradeeptathineni/blueprint-ai">
<summary><a href="https://github.com/pradeeptathineni/blueprint-ai"><strong>Blueprint AI</strong></a> — Use deterministic tools to set up project foundations and engineering checks.</summary>

|              |                                                                                                                |
| :----------- | :------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _inspect → plan → create or evolve → review → verify_                                                          |
| **Maturity** | `Experimental` · [`0.9.0`](https://github.com/pradeeptathineni/blueprint-ai/releases/tag/0.9.0) · TRL 3        |
| **Status**   | Working CLI for project creation, inspection, review, and evolution. Optional model reasoning remains bounded. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `devtools` ; `python` ; `engineering`                                                                          |

</details>

<details data-repo="pradeeptathineni/intentional-ai">
<summary>🔒 <strong>Intentional AI</strong> — Schedule deliberate local work and retain its state.</summary>

|              |                                                                                                    |
| :----------- | :------------------------------------------------------------------------------------------------- |
| **Flow**     | _approved intent → schedule → bounded work → verify → retain state_                                |
| **Maturity** | `Experimental` · Private · TRL 2                                                                   |
| **Status**   | Private scheduling and Git-control experiments exist. A wider orchestration role remains proposed. |
| **Activity** | Updated 2026-09-13 · `Quiet` |
| **Tags**     | `automation` ; `scheduling` ; `python`                                                             |

</details>

<details data-repo="pradeeptathineni/maestro-ai">
<summary>🔒 <strong>Maestro AI</strong> — Execute approved work with checks and a reviewable handoff.</summary>

|              |                                                                                    |
| :----------- | :--------------------------------------------------------------------------------- |
| **Flow**     | _approved task → isolated checkout → execute → check → review_ |
| **Maturity** | `Experimental` · `v0.1.0-alpha.1` · Private · TRL 4 |
| **Status**   | Local task series retain work and scoped commits for review. Run controls flag work needing attention and bind cancellation to its run identity. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `orchestration` ; `python` |

</details>

<details data-repo="pradeeptathineni/deep-ai">
<summary>🔒 <strong>Deep AI</strong> — Bring research, planning, writing and execution into one desktop workspace.</summary>

|              |                                                                                        |
| :----------- | :------------------------------------------------------------------------------------- |
| **Flow**     | _research → compare → plan → build → review_ |
| **Maturity** | `Experimental` · `v0.1.0-alpha.1` · Private · TRL 4 |
| **Status**   | A working local UI connects the other projects' capabilities, including retained evidence, writing feedback and managed execution. |
| **Activity** | Updated 2026-10-24 · `Recent` |
| **Tags**     | `ai` ; `desktop` ; `react` ; `typescript` |

</details>

</dd></dl>

`#` The idea: each project should be useful on its own and work with the others in one engineering workspace.

</details>

<p></p>

<details open>
<summary>self.projects.group(<strong>"<ins>Practice and Exploration</ins>"</strong>)</summary>

<p></p>

<dl><dd>

<details data-repo="pradeeptathineni/labs">
<summary><a href="https://github.com/pradeeptathineni/labs"><strong>Labs</strong></a> — Practice problem-solving and share the work behind it.</summary>

|              |                                                                                                                              |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _problem → investigate → build or explain → reflect → catalog_                                                               |
| **Maturity** | `Experimental`                                                                                                               |
| **Status**   | [Published catalog](https://pradeeptathineni.github.io/labs/) separates actual practice from exercises still waiting for me. |
| **Activity** | Updated 2026-10-12 · `Recent`                                                                                                |
| **Tags**     | `practice` ; `code` ; `study` ; `writing`                                                                                    |

</details>

<details data-repo="pradeeptathineni/home-lab">
<summary><a href="https://github.com/pradeeptathineni/home-lab"><strong>Home Lab</strong></a> — Learn what useful private services need before moving to a dedicated server.</summary>

|              |                                                                                                                                |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _provision → run services → observe → test recovery → refine_                                                                  |
| **Maturity** | `Experimental`                                                                                                                 |
| **Status**   | Mac-hosted Linux lab with monitoring, local AI, and disposable experiments. An independent backup destination is still needed. |
| **Activity** | Updated 2026-10-03 · `Recent`                                                                                                  |
| **Tags**     | `homelab` ; `linux` ; `local-ai` ; `observability`                                                                             |

</details>

<details data-repo="pradeeptathineni/nature-of-code">
<summary><a href="https://github.com/pradeeptathineni/nature-of-code"><strong>Nature of Code</strong></a> — Explore visual systems through creative coding.</summary>

|              |                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _idea → simulation → observe → change rules → repeat_                                                                            |
| **Maturity** | `Experimental`                                                                                                                   |
| **Status**   | Terrain, starfields, fireworks, and other sketches inspired by Daniel Shiffman and Coding Train. An older experiment collection. |
| **Activity** | Updated 2023-06-12 · `Quiet`                                                                                                     |
| **Tags**     | `p5.js` ; `simulation` ; `creative-coding`                                                                                       |

</details>

</dd></dl>

</details>

<p></p>

<details open>
<summary>self.projects.group(<strong>"<ins>Learning</ins>"</strong>)</summary>

<p></p>

<dl><dd>

<details data-repo="pradeeptathineni/uta-mccombs-ai-ml">
<summary><a href="https://github.com/pradeeptathineni/uta-mccombs-ai-ml"><strong>UT Austin McCombs AI/ML</strong></a> — Apply machine learning and generative AI to business problems through coursework.</summary>

|              |                                                                                                                  |
| :----------- | :--------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _business problem → explore data → model → evaluate → recommend_                                                 |
| **Maturity** | `Experimental`                                                                                                   |
| **Status**   | Course projects run from Python analysis to agents. Some include my notebooks; the program is still in progress. |
| **Activity** | Updated 2026-10-12 · `Recent`                                                                                    |
| **Tags**     | `ml` ; `generative-ai` ; `python` ; `coursework`                                                                 |

</details>

<details data-repo="pradeeptathineni/jhu-whiting-agentic">
<summary><a href="https://github.com/pradeeptathineni/jhu-whiting-agentic"><strong>Johns Hopkins AI and Agentic AI Engineering</strong></a> — A home for planned coursework on building and operating ML and agent systems.</summary>

|              |                                                                       |
| :----------- | :-------------------------------------------------------------------- |
| **Flow**     | _assignment → build → evaluate → document_                            |
| **Maturity** | `Idea`                                                                |
| **Status**   | The program is planned and my cohort is unconfirmed. No projects yet. |
| **Activity** | Updated 2026-10-12 · `Recent`                                         |
| **Tags**     | `ai` ; `agents` ; `coursework`                                        |

</details>

<details data-repo="pradeeptathineni/ai-engineering-from-scratch">
<summary><a href="https://github.com/pradeeptathineni/ai-engineering-from-scratch"><strong>AI Engineering from Scratch</strong></a> — My fork of an open AI engineering curriculum, kept for study.</summary>

|              |                                                                                                                                         |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Flow**     | _learn → build → ship_                                                                                                                  |
| **Maturity** | `Experimental`                                                                                                                          |
| **Status**   | Fork of [rohitg00's curriculum](https://github.com/rohitg00/ai-engineering-from-scratch). Lessons and code are upstream work, not mine. |
| **Activity** | Updated 2026-09-07 · `Quiet`                                                                                                            |
| **Tags**     | `ai` ; `curriculum` ; `fork`                                                                                                            |

</details>

</dd></dl>

</details>
<br/>

## <a name="tech-stack"></a>🛠️ def tech_stack(self, sort=[ "preference", "experience" ]):

<details>
<summary>self.tech.info()</summary>

<p></p>

`#` Items marked `*like this*` are the tools I reach for most often.

</details>

<p></p>

<details>
<summary>self.tech.group(<strong>"<ins>Systems</ins>"</strong>)</summary>

<p></p>

- **Operating Systems** — `*macOS*` ; `*Linux*` ; `Windows`
- **Editors / Notebooks** — `*VS Code*` ; `Jupyter` ; `Google Colab`

</details>

<p></p>

<details open>
<summary>self.tech.group(<strong>"<ins>Software &amp; Platforms</ins>"</strong>)</summary>

<p></p>

- **Code** — `*Python*` ; `*Bash*` ; `Go` ; `JavaScript` ; `TypeScript` ; `Node.js` ; `SQL` ; `React`
- **Cloud & Platform** — `*AWS*` ; `*Docker*` ; `Kubernetes` ; `Helm`
- **Infrastructure as Code** — `*Terraform*` ; `OpenTofu` ; `AWS CloudFormation`
- **Delivery** — `*Git*` ; `*GitHub Actions*` ; `CircleCI` ; `AWS CodePipeline` ; `Jenki...nvm`
- **Observability** — `CloudWatch` ; `Prometheus` ; `Grafana` ; `ELK`
- **AI Tooling** — `*Codex*` ; `*ChatGPT*` ; `Claude Code` ; `Claude`

</details>

<p></p>

<details>
<summary>self.tech.group(<strong>"<ins>Focuses</ins>"</strong>)</summary>

<p></p>

- **Engineering** — `Automation` ; `DevOps` ; `Cloud Architecture` ; `Platform Engineering` ; `Solutions Architecture` ; `Modernization` ; `Customer Enablement` ; `Developer Tooling` ; `OSS / Prior-Art Discovery` ; `IoT`
- **AI** — `LLM Applications` ; `RAG` ; `Agents` ; `Context Engineering` ; `Model Routing` ; `Evaluation` ; `Machine Learning`
- **Exploring** — `Computer Vision` ; `Data Visualization` ; `Simulation`

</details>
<br/>

## 🟢 def neon1(self, type="business", redirect=True):

`#` [**neon1**](https://github.com/neon1llc) is my engineering organization, focused on software, infrastructure, and automation for small and midsize businesses.\
`#` I share reusable tools and patterns through its public repositories.\
`#` AWS CLI Plus lives there.

<br/>

## 🗂️ class Meta(Deep):

<details>
<summary>def disclaimers(self, warnings="alert"):</summary>

<p></p>

- **Readiness and evidence** — Experimental releases aren't proof of production readiness. Tests and internal measurements support specific claims; broader value, usefulness, and independent review need their own evidence.
- **Activity** — Commit dates are snapshots, not maintenance commitments. `Quiet` doesn't mean abandoned.
- **Private and planned work** — 🔒 marks a private repository with a public description. Planned work describes intentions; the Status row explains what is implemented.
- **Reuse and credits** — Software and [artwork](assets/README.md) retain their own licenses and permissions. I preserve required attribution and notices; this profile grants no additional reuse rights. Check the terms before adopting or running anything.
- **AI assistance** — I use AI for research, planning, implementation, and review. I remain responsible for verification and results.

</details>

<p></p>

<details>
<summary>def thoughts(self, think=2, filter=None, humor="dry"):</summary>

<p></p>

`state` = `self.self()`

<p></p>

`sanity` = "Sanity is like a spectacular readme. They both heavily collapse."

<p></p>

`is_this_a_joke_r` = "You either die a standard, or live long enough to see yourself become a **_🌟spectacle✨_**."

<p></p>

`superfluously` = "An overengineered custom semantic that works great for me but retains personal value only through bias, while being generally frustrating for anyone else, is a private joke. A similar extreme is spending twenty minutes building a condiment passing system when someone asked for the salt."

<details>
<summary>self.imagine(superfluously)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/0974-the-general-problem.png" alt="A request to pass the salt becomes a twenty-minute effort to build a general condiment-passing system." width="550"><br/>
  <sup><em><a href="https://xkcd.com/974/">XKCD #974</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`basic` = "If you've ever thought about building a habit tracker, to-do app, or productivity tool, you might just be an engineer."

<p></p>

`cliche` = "If you've ever used 5x, 10x, or similar to describe productivity gain, you might just be an idiot."

<p></p>

`overzealous` = "If you haven't spent a whole Sunday on one readme, can you really call yourself an engineer?"

<p></p>

`fixing_problems` = "Within the problem set, each problem's solution comes with its own set of problems. "

```python
while(fixing_problems): fixing_problems += fixing_problems
```
> _MemoryError_

<details>
<summary>❌ self.imagine(fixing problems)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/1739-fixing-problems.png" alt="An engineer explains a chain of problems created while fixing earlier problems." width="312"><br/>
  <sup><em><a href="https://xkcd.com/1739/">XKCD #1739</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`automation` = "Spend all day automating a five-minute task, spend tomorrow repairing the automation. Time spent to earn time saved becomes a matter of faith, and I call that a long-term investment."

<details>
<summary>self.imagine(automation)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/1319-automation.png" alt="Two work-versus-time graphs contrast automation's promised free time with debugging, rethinking, and ongoing development." width="404"><br/>
  <sup><em><a href="https://xkcd.com/1319/">XKCD #1319</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`autonomy` = "No matter how smart or independent, every autonomous system still ends up needing human intervention. I s'pose we're not so different from them."

<p></p>

`machine_learning` = """\\\
1\. Get data.\
2. Check data out, head to tail.\
3. Analyze data's patterns.\
4. Get to know data completely; build model judgements.\
5. Predict next moves with model judgments; if data agrees, continue.\
6. Continuously predict next moves, classify new outcomes, and reassess judgments.\
7. Marry data, maybe have some child processes, grow stale together.\
"""

<details>
<summary>self.imagine(machine_learning)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/1838-machine-learning.png" alt="Data enters a pile of linear algebra. An engineer stirs the pile until the answers look right." width="371"><br/>
  <sup><em><a href="https://xkcd.com/1838/">XKCD #1838</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`ai` = "Just sum wild, curious times, pardna."

<details>
<summary>self.imagine(ai)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/0789-showdown.png" alt="Two cowboys prepare for a duel, but a tumbleweed draws two guns and wins the showdown." width="740"><br/>
  <sup><em><a href="https://xkcd.com/789/">XKCD #789</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`originality` = "Nothing humbles an original idea like a 10 year old GitHub repo that already does it, has better documentation, and can run on a 2004 model Raspberry Pi. That's just discovery."

<p></p>

`personal_projects` = "I chose the use cases. I wrote the code. I decided the golden set for success and tested. My tests passed, yet I keep all claims on probation. I accept new claims for good measure. That is a lot of authority given to myself from myself trying to prove myself to myself."

<details>
<summary>self.imagine(personal_projects)</summary>

<p></p>

<p align="center">
  <img src="assets/xkcd/0882-significant.png" alt="Scientists test many jelly-bean colors. One apparent association produces an exaggerated news headline." width="540"><br/>
  <sup><em><a href="https://xkcd.com/882/">XKCD #882</a> by Randall Munroe · <a href="https://creativecommons.org/licenses/by-nc/2.5/">CC BY-NC 2.5</a>.</em></sup>
</p>

</details>

<p></p>

`research` = "Knowing all my options is paramount. Unfortunately, ‘keep researching’ is always one of them, and it comes with an unlimited free trial. Eventually I have to choose something and find out what I missed."

<p></p>

`dashboards` = "Every dashboard is green, every failed test is a pass, and every benchmark is a record with Inspect Element and a few minutes. Show me what survives a refresh."

<p></p>

`impact` = "The world does not owe my side project a use case. If nobody needs it, I can still enjoy building it. I just don't get to rename my enjoyment ‘impact’ and expect everyone else to agree."

</details>

<p></p>

<details>
<summary>def self(self, true=False):</summary>

<p></p>

<p align="center">
  <img src="assets/this-is-fine.png" alt="Two panels of a dog sitting with a mug in a burning room, saying ‘This is fine.’" width="460"><br/>
  <sup><em>This is fine · <a href="https://gunshowcomic.com/648">KC Green / Gunshow</a></em></sup>
</p>

</details>

<p></p>

<details>
<summary>def self(self, true=True):</summary>

<p></p>

<p align="center">
  <img src="assets/brain-explosion.jpg" alt="A man in glasses holds his hands beside his head as a cosmic explosion fills the background." width="460"><br/>
  <sup><em>Brain explosion · <a href="https://meme-arsenal.com/create/template/11175240">Meme Arsenal template</a>.</em></sup>
</p>

</details>
<br/>
<br/>
<br/>

---

[EOF]: :c-l>lF%H5o5CnU_Vmlh-FCge>5FPa;UMYxhC)pQ_f1d;)NIRNY?RBIS;zHY_*@Qt}gd03h#qnee;Wo5G2q*S3E#^<^NJX-$@PT<V@ldM^6Gt{l8^*WvJ~q^ke|Jz*i8yM)`Csh{)ch;0Z58$PQpY$0Xw5t&
