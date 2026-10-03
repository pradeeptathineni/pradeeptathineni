# Hi, I'm Pradeep 👋

I'm an engineer who sees repeated work as a design problem: if I have to do it twice, I start asking why the computer isn't doing it.

```text
Once is flirtation. Twice is frustration.
Once is temptation. Twice is libation.
Once is foundation. Twice is causation.

All thereafter is automation.
```

I build cloud infrastructure, developer tools, automation, AI systems, and the occasional visual experiment. The common thread is straightforward: make useful work easier to repeat, inspect, and trust.

## 🤖 A candid note about the AI work

> The robots have been prolific. That does not make every repository impressive.

Several of my recent projects are deliberately **AI-heavy**. I set the problem, constraints, priorities, acceptance criteria, and review loop; models help design the system and produce much of the implementation and documentation; then I inspect results, challenge claims, tighten the constraints, and repeat. They are case studies in cyclical AI-assisted development—not a claim that I personally typed, originated, or deeply understood every line on the first pass.

Some generated output is useful. Some is sophisticated-looking slop. A large diff is not a large accomplishment, and green checks do not automatically make a project valuable. What matters is what survives ordinary engineering scrutiny: a real problem, explicit boundaries, reproducible behavior, honest evidence, and something another person can actually use or learn from.

I label projects on two separate axes so the newer AI work does not bury stronger or more representative engineering:

| Label | Meaning |
| --- | --- |
| **Substantial** | Developed implementation, documentation, tests or automation, and enough history to evaluate seriously. This does not mean “production-ready.” |
| **Working** | Runnable and useful within its stated scope, but still evolving. |
| **Experimental** | A prototype or case study. Judge the method and evidence, not the amount of generated code. |
| **Learning / legacy** | Older, narrower, or intentionally lightweight work kept for context rather than presented as current flagship engineering. |
| **Human-led** | Primarily built through direct, hands-on development rather than my current agent-driven workflow. |
| **AI-assisted** | AI contributed materially, while the project remains human-directed and reviewed. |
| **AI-heavy** | Most—or nearly all—of the recent implementation and/or documentation was generated or substantially transformed by AI under human direction and review. |
| **Fork** | Upstream work retained for learning or reference; I do not claim authorship. |

I am not publishing percentages because I do not have trustworthy line-level provenance for every repository. A precise-looking “93% AI” would be theater. **AI-heavy** is the honest claim I can support today.

## ⭐ Start here

These are the public projects I would put in front of someone first.

| Project | Why it is worth seeing | Maturity | Provenance |
| --- | --- | --- | --- |
| [**AWS Terraform Engineering Challenge**](https://github.com/pradeeptathineni/eng-challenge-aws-terraform) | A Terraform-defined AWS web stack with modular networking, optional protected remote state, CI, deployment verification, safe teardown, and the engineering decisions preserved alongside the implementation. | **Substantial** | **AI-assisted** |
| [**AWS CLI Plus**](https://github.com/neon1llc/aws-clip) | A Go wrapper around AWS CLI v2 that makes multi-profile identity visible and adds account-bound guards around risky commands without pretending to replace the AWS CLI. | **Working** | **AI-heavy** |
| [**home-lab**](https://github.com/pradeeptathineni/home-lab) | A measured, private home-lab implementation on real hardware: services, observability, local AI, backup practice, and disposable experiments, with the unfinished parts stated plainly. | **Working** | **AI-heavy** |
| [**nature-of-code**](https://github.com/pradeeptathineni/nature-of-code) | Older creative-coding exercises in simulation, terrain, starfields, fireworks, moiré patterns, and wave-function collapse. Messier than a polished demo, but recognizably hands-on learning. | **Learning / legacy** | **Human-led** |

## 🟢 neon1

[**neon1**](https://github.com/neon1llc) is the public home for practical tools that may deserve an identity beyond my personal experiments: software, automation, infrastructure, IoT, and grounded uses of AI intended to make work or life easier.

It is small on purpose. I am not presenting a one-tool organization as an empire. [AWS CLI Plus](https://github.com/neon1llc/aws-clip) is its first public tool and the current example of the standard: solve a concrete problem, reuse the authoritative platform underneath, make risk visible, and document the limits.

## 🧪 AI-heavy case studies

These repositories explore whether iterative AI-assisted development can produce work that holds up after the novelty and output volume wear off. They contain real implementations and checks, but they are also experiments. Read the stated boundaries before reading ambition into them.

| Project | What is actually being tested | Maturity | Provenance |
| --- | --- | --- | --- |
| [**ShouldaUsedThat**](https://github.com/pradeeptathineni/shoulda-used-that) | Whether a deterministic CLI and evidence ledger can make “reuse, extend, or build” decisions more explicit before more software is created. | **Working** | **AI-heavy** |
| [**Blueprint AI**](https://github.com/pradeeptathineni/blueprint-ai) | Reusable engineering blueprints for inspecting, reviewing, creating, and evolving software with native tools, deterministic checks, and bounded model reasoning. | **Working** | **AI-heavy** |
| [**Context AI**](https://github.com/pradeeptathineni/context-ai) | Whether reusable context can stay concise, reviewable, provider-aware, and testable instead of becoming one enormous prompt. | **Working** | **AI-heavy** |
| [**Maestro AI**](https://github.com/pradeeptathineni/maestro-ai) | Evidence-bound research across live search and a durable corpus, including provenance, replay, abstention, and explicit gaps in validation. | **Experimental** | **AI-heavy** |
| [**Principles AI**](https://github.com/pradeeptathineni/principles-ai) | An evidence-grounded knowledge system for durable principles and practices, with deterministic structure around human-governed semantic judgment. | **Experimental** | **AI-heavy** |

The value in these projects, where it exists, is not “look how much code AI made.” It is the record of problem framing, constraints, failed assumptions, verification, and the boundary between what a deterministic system can prove and what still requires human judgment.

## 🗂️ The rest of the public shelf

Not every public repository is a portfolio piece, so here is the unglamorous version:

| Repository | Honest status |
| --- | --- |
| [**aws-iac-terraform**](https://github.com/pradeeptathineni/aws-iac-terraform) | A minimal Terraform starter, not a mature infrastructure project. See the engineering challenge above for the more representative work. |
| [**system**](https://github.com/pradeeptathineni/system) | A legacy personal shell configuration, kept as history rather than current guidance. |
| [**ai-engineering-from-scratch**](https://github.com/pradeeptathineni/ai-engineering-from-scratch) | A public fork of [Rohit Ghumare's upstream project](https://github.com/rohitg00/ai-engineering-from-scratch), retained for learning. It is not my original work. |

## 🔎 Prior art first

Generating code is cheap; knowing whether more code should exist is harder.

My [GitHub Stars](https://github.com/pradeeptathineni?tab=stars) are organized as a working prior-art map. A star means **worth considering or revisiting**, not that I have fully audited or adopted the project.

- **AI + knowledge:** [Generative AI & Agents](https://github.com/stars/pradeeptathineni/lists/generative-ai-agents) · [RAG, Search & Knowledge](https://github.com/stars/pradeeptathineni/lists/rag-search-knowledge) · [Computer Vision & Multimodal](https://github.com/stars/pradeeptathineni/lists/computer-vision-multimodal)
- **Engineering + delivery:** [Cloud Infrastructure & IaC](https://github.com/stars/pradeeptathineni/lists/cloud-infrastructure-iac) · [Platform Engineering & Delivery](https://github.com/stars/pradeeptathineni/lists/platform-engineering-delivery) · [Software Supply Chain](https://github.com/stars/pradeeptathineni/lists/software-supply-chain) · [Python Engineering](https://github.com/stars/pradeeptathineni/lists/python-engineering) · [Web Engineering & Interfaces](https://github.com/stars/pradeeptathineni/lists/web-engineering-interfaces)
- **Systems + exploration:** [Homelab & Self-Hosting](https://github.com/stars/pradeeptathineni/lists/homelab-self-hosting) · [Creative Coding & Visualization](https://github.com/stars/pradeeptathineni/lists/creative-coding-visualization) · [Nature, Physics & Simulation](https://github.com/stars/pradeeptathineni/lists/nature-physics-simulation) · [OSS Curation & Prior Art](https://github.com/stars/pradeeptathineni/lists/oss-curation-prior-art)

Where a star is not enough, the [ShouldaUsedThat catalog](https://pradeeptathineni.github.io/shoulda-used-that/curation/) keeps the evidence, rationale, freshness, disposition, and conditions that would make a decision worth revisiting.

## 🧭 How I think

I like turning laborious physical- or digital-world processes into systems that are faster, more reliable, and easier to understand.

| Domain | Question I keep asking |
| --- | --- |
| Software | **Does this create meaningful user value?** |
| Automation | **What steps can be removed, collapsed, or made reliable?** |
| Infrastructure | **Does this shorten and strengthen the feedback loop?** |
| Hardware / IoT | **Where can software make a physical system meaningfully better, and vice-versa?** |
| AI | **What can be grounded, bounded, and independently verified?** |

They all reduce to the same question: **How can I build provable, repeatable, reliable technology that makes people's lives easier—or at least makes an interesting problem more understandable?**

## 🛠️ Stack

**Primary:** Python · Go · JavaScript/Node.js · Terraform/HCL · Bash · AWS · Git · GitHub Actions

**Also:** Docker · Kubernetes · React · retrieval/agents · computer vision · Processing/p5.js · simulation · data visualization

---

[EOF]: :c-l>lF%H5o5CnU_Vmlh-FCge>5FPa;UMYxhC)pQ_f1d;)NIRNY?RBIS;zHY_*@Qt}gd03h#qnee;Wo5G2q*S3E#^<^NJX-$@PT<V@ldM^6Gt{l8^*WvJ~q^ke|Jz*i8yM)`Csh{)ch;0Z58$PQpY$0Xw5t&
