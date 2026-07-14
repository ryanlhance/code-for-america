#!/usr/bin/env python3
"""Generates data.json for the Code for America fit-map page.
Single source of truth: edit this, run `python3 build_data.py`, and data.json
is rewritten. (Or just edit data.json directly — this is a convenience.)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Portfolio public URLs (piece -> hance.work case study) ----
PF = {
    "ev-pf-blueprint-local":   "https://www.hance.work/Local-Enterprise-Level-Service-Blueprint-74f9ecfa9f4a4873be1b909a7f5e37d8?pvs=25",
    "ev-pf-eraf":              "https://www.hance.work/Systems-Flow-ERAF-Map-74cfa7e910564777a9883a55f066d4f9?pvs=25",
    "ev-pf-blueprint-global":  "https://www.hance.work/Global-Enterprise-Level-Service-Blueprint-cd937db4cb344b318bae4c6d1e7ca9fa?pvs=25",
    "ev-pf-journey":           "https://www.hance.work/Global-Journey-Mapping-Effort-228e643935ea43aab50ee95d8f56305f?pvs=25",
    "ev-pf-cdp":               "https://www.hance.work/Customer-Data-Platform-Roadmap-0d65a3c99943497e9c969160e33742a2?pvs=25",
    "ev-pf-ai-roadmap":        "https://www.hance.work/A-I-Product-Roadmap-d042f4d986e5441bbb80b5e5ea4bd018?pvs=25",
    "ev-pf-platform-playbook": "https://www.hance.work/Platform-Design-Playbook-838ea8da681f4577bce28f0ea7e30b67?pvs=25",
    "ev-pf-genai-playbook":    "https://www.hance.work/Generative-A-I-Playbook-bb68ca8c80d840e5be083136a0b88f92?pvs=25",
    "ev-pf-personas":          "https://www.hance.work/A-I-Persona-Prototypes-43575337f52c4cecaf4fdd871e5aa41e?pvs=25",
    "ev-pf-usertesting":       "https://www.hance.work/User-Testing-Strategic-Recommendations-9f073d6ea0bb4bd1bef08d176895dd10?pvs=25",
    "ev-pf-legacyux":          "https://www.hance.work/Legacy-Software-UX-Strategy-e189dab0fccc4d088f0f8e2a22b009a9?pvs=25",
    "ev-pf-prompt":            "https://www.hance.work/Prompt-Engineering-Strategic-Design-40891c882c00477e936743a5d0657ddc?pvs=25",
    "ev-portfolio":            "https://www.hance.work/",
}

# ---- Evidence (title + text shown to the reader) ----
evidence = {
  # -- service design depth --
  "ev-sd-years": {"title": "7+ Years of Service Design", "text": "7+ years specifically in service design, but 13+ years designing how people move through complex products, services, and operations — including senior service design and design strategy roles across Bayer Crop Science's $27B division."},
  "ev-service-blueprint": {"title": "Service Blueprinting", "text": "Built service blueprints at every scale: Bayer's 20,000+ point global enterprise blueprint, and the 450-point blueprint of my own startup that became the information architecture for executive decision making."},
  "ev-bayer-journey": {"title": "Global Journey Mapping", "text": "Facilitated a global journey mapping effort spanning North America, Europe, and Asia-Pacific — 2,250 journey points across 27 teams — that cut environmental toxin risk 70% and raised workplace safety 30% within two quarters."},
  "ev-site-rebuild": {"title": "End-to-End Site Rebuild", "text": "UX Lead on Bayer's end-to-end customer site rebuild, from the public marketing pages through the logged-in customer portal — driving a 35% increase in product and service opportunities and leading user acceptance testing across the North American user base."},
  "ev-discovery": {"title": "Discovery & Research", "text": "Discovery is where I start every engagement: ethnographic field research, stakeholder interviews, contextual inquiry, and journey mapping to turn workforce challenges into actionable solutions."},
  "ev-counseling-restructure": {"title": "Nationwide Restructuring", "text": "Led the nationwide restructuring of a counseling franchise — grounded in ethnographic interviews with the corporate team and franchisees — and reorganized the corporate team with zero layoffs, using a research-driven decision tool I built."},
  "ev-eraf": {"title": "Systems Mapping", "text": "At Dryland, employees were ready to quit over 'bad communication.' Ethnographic research showed the real problem: they couldn't see the larger business system. I built an ERAF map of 100+ interaction points that let siloed teams see their role in the whole — and they stayed."},
  "ev-metrics": {"title": "Metrics Fluency", "text": "Fluent in success metrics: OKRs, KPIs, adoption rate, time-to-launch, satisfaction. Drove measurable outcomes like a 35% lift in product and service opportunities, a 30% rise in workplace safety, and 2% to 26% platform adoption in two months."},
  "ev-ad-constraints": {"title": "Working Within Constraints", "text": "As an assistant director, my whole job was making the director's vision possible despite budget, time, and resource constraints — I developed the concept and vision, roadmapped, and implemented the operational plan across 40 productions."},
  "ev-ags-blueprint": {"title": "Tech-Stack Blueprinting", "text": "Created an end-to-end service blueprint for a hospitality franchise to determine the tech stack roadmap for multi-location build-outs."},
  "ev-system-not-symptom": {"title": "Root-Cause Solving", "text": "I will spend an entire day on a single problem — solving the system instead of the symptom — because I know it will save days of time in the future."},

  # -- multiple workstreams / pace --
  "ev-bayer-flux": {"title": "Multiple Workstreams", "text": "My role at Bayer was constantly in flux, in the best way: UX lead for the farmer experience, design strategist for the operations platforms, then lead strategist for the generative AI effort — design leaders kept passing me around a 25,000-person division."},
  "ev-film-producer": {"title": "Concurrent Project Management", "text": "Owned productions end to end as the client's point of contact, delivering on time and on budget while running an average of six concurrent productions, peaking at ten to twelve."},
  "ev-parallel": {"title": "Parallel Workloads", "text": "Built a startup to a profitable exit while working Bayer full time — Bayer was my 9-to-5, the startup was my 5-to-9."},
  "ev-rampfast": {"title": "Rapid Domain Learning", "text": "Walked into a Fortune 500 knowing nothing about agriculture and was shipping across four platforms within a year."},
  "ev-agile": {"title": "Agile Experience", "text": "Worked inside agile product teams across four Bayer platforms: refined backlogs, aligned hundreds of technical stories to user needs, led user acceptance testing across the North American user base, and built out the scrum board — writing all the stories and leading scrum — for a legacy platform team."},

  # -- collaboration / facilitation / communication --
  "ev-delta-pm": {"title": "Cross-Functional Leadership", "text": "Product Manager on a Delta Air Lines engagement: led a cross-cultural team spanning eight countries and nine disciplines, owned budget, timelines, and stakeholder relationships, and was the primary contact between client and team — presenting regularly in Delta's corporate rooms."},
  "ev-translator": {"title": "Cross-Discipline Fluency", "text": "Fluent in business, design, and engineering languages: translating business jargon to design requirements, engineering capabilities to business possibilities, and design visions to engineering roadmaps."},
  "ev-facilitation": {"title": "Workshop Facilitation", "text": "Facilitated hundreds of design thinking workshops from 5 to 150 people, and was selected by Miro as the sole Enterprise Advocate for all of Bayer — a company of ~100,000 people."},
  "ev-exec-alignment": {"title": "Executive Alignment", "text": "Developed an agentic AI experience at Bayer and sold it internally to senior executives: months of workshops, demos, and one-on-one influencing, navigating the political complexity of enterprise decision making before getting the greenlight to build."},
  "ev-ags-consulting": {"title": "Strategic Advising", "text": "As a consultant to franchisees and franchisors, I build relationships, influence, and drive the strategic alignment needed to get the opportunity to design new systems and lead enterprise transformation."},
  "ev-writing": {"title": "Strategic Writing", "text": "A decade writing 20 to 50 pages a week, from user stories to executive strategy; authored Bayer's Universal Design Principles, adopted across every platform in the division."},
  "ev-10industries": {"title": "10+ Industries", "text": "Experience across 10+ industries and hundreds of niche personas; the service-design and operations skillset transfers to any business domain."},

  # -- mentorship / team health --
  "ev-mentor": {"title": "Mentorship Experience", "text": "Ran training and development for a 250-person camp staff — a redesigned program that lifted retention 67% year over year, am a trained and practicing leadership coach, and spent six years in film identifying underutilized talent, developing them through on-set mentor matching, and launching them to lead their own crews."},
  "ev-eq": {"title": "Strengths Coaching", "text": "Gallup-certified Strengths Coach trained in behavior and relationship psychology; taught empathy and emotional intelligence professionally through years of leadership development."},
  "ev-adoption": {"title": "2% to 26% Adoption", "text": "Took a Fortune 500's internal AI platform from 2% to 26% adoption in two months by building the playbook and training that got people to actually use it."},
  "ev-ai-playbook-langs": {"title": "Global AI Training", "text": "Authored Bayer's AI Strategy Playbook and led its global dissemination in 20+ languages to thousands of internal users across business, engineering, design, and HR."},
  "ev-playbooks": {"title": "Playbook Writing", "text": "An operations playbook that cut resource needs 60%, a startup playbook library that lifted efficiency 80%, and a Fortune 500 AI strategy playbook shipped in 20+ languages."},

  # -- mission / service --
  "ev-mission-service": {"title": "Servant Leadership", "text": "Seven summers on staff at a summer camp serving thousands of kids, leadership development practice for high school and college students, and cohort-based men's work currently."},
  "ev-systems-for-people": {"title": "Systems Thinking", "text": "My brain operates in the unseen, constantly mapping, blueprinting, and writing the playbooks for the iceberg people only see the tip of."},
  "ev-bananas": {"title": "Experience Design", "text": "First hire on the Savannah Bananas entertainment team: designed and executed the Fans First experiences and promotional campaigns the company standardized and scaled with, contributing to a 500% social awareness surge and the first sold-out season of 250,000 fans."},
  "ev-dryland-scale": {"title": "Organizational Transformation", "text": "Chief of staff who scaled Dryland, a construction-science startup, from one client to a profitable exit. One org redesign — detaching the CEO from day-to-day work — doubled revenue and quadrupled headcount in three months."},
  "ev-responsible-ai": {"title": "Responsible AI", "text": "I've been integrating AI into human systems since before commercial integrations existed — agentic personas validated by 20+ year subject-matter experts above 80% accuracy before teams were allowed to rely on them, and stakeholder AI education from Indonesia to Brazil."},

  # -- education / logistics --
  "ev-scad": {"title": "Service Design M.A.", "text": "M.A. in Creative Business Leadership from SCAD's De Sole School of Business Innovation — essentially an MBA crossbred with service design, built for intrapreneurship and using design thinking to influence decision making."},
  "ev-travel": {"title": "Happy to Travel", "text": "Would love to. 20 to 30% on the road genuinely works for me — 10% is easy."},

  # ---- Portfolio pieces (public case studies) ----
  "ev-portfolio": {"title": "Full Portfolio", "text": "Twelve public case studies across service blueprints, journey maps, systems maps, AI strategy, and UX — each one walks through the process, the deliverables, and the impact."},
  "ev-pf-blueprint-global": {"title": "Global Enterprise Service Blueprint", "text": "Bayer's 20,000+ point global service blueprint mapping tech, personas, and interactions across countries to surface redundancies and gaps."},
  "ev-pf-blueprint-local": {"title": "Local Enterprise Service Blueprint", "text": "A focused enterprise service blueprint mapping a business's systems and interaction points end to end."},
  "ev-pf-journey": {"title": "Global Journey Mapping Effort", "text": "A 27-team global journey map producing 2,250 journey points and new processes on a confidential European compliance project."},
  "ev-pf-cdp": {"title": "Customer Data Platform Roadmap", "text": "The use cases and roadmap, built from the customer-experience perspective, that anchored a Fortune 500's Customer Data Platform vendor selection."},
  "ev-pf-usertesting": {"title": "User Testing Strategic Recommendations", "text": "Using user research and testing to inform strategic product development on a supply chain platform."},
  "ev-pf-legacyux": {"title": "Legacy Software UX Strategy", "text": "Restructured forms, progress indicators, and language to make a legacy platform more efficient and usable."},
  "ev-pf-genai-playbook": {"title": "Generative A.I. Playbook", "text": "The AI strategy playbook that drove adoption from 2% to 26%, shipped in 20+ languages to thousands of users."},
  "ev-pf-platform-playbook": {"title": "Platform Design Playbook", "text": "A reusable playbook for designing and standing up new platforms."},
  "ev-pf-personas": {"title": "A.I. Persona Prototypes", "text": "Agentic AI personas wired into Microsoft Teams — built before commercial AI integrations existed and launched across multiple company-wide platforms — so teams could interview user models they couldn't otherwise reach."},
  "ev-pf-ai-roadmap": {"title": "A.I. Product Roadmap", "text": "Product roadmap for a Fortune 500's internal AI platform, defining the use cases and the path to adoption."},
  "ev-pf-prompt": {"title": "Prompt Engineering Strategic Design", "text": "A prompt engineering approach and template that let non-technical stakeholders across the company use generative AI effectively for the first time."},
  "ev-pf-eraf": {"title": "Systems Flow (ERAF) Map", "text": "A systems-flow map of 100+ interaction points that helped siloed teams see their role in the larger business — and kept employees who were ready to quit over 'bad communication.'"},
}
# attach portfolio links
for k, url in PF.items():
    evidence[k]["link"] = url

def ph(pid, text, ev):
    return {"id": pid, "text": text, "evidence": ev}

# ---- The job description, as real prose with inline highlighted phrases ----
jd_prose = [
  {"type": "p", "segments": [
    "Code for America believes government can work for the people, by the people, in the new digital age, and that government at all levels can and should work well for all people. For more than a decade, we've worked to show that with the mindful use of technology, we can ",
    ph("p-community-needs", "break down barriers, meet community needs, and find real solutions",
       ["ev-mission-service", "ev-systems-for-people", "ev-eraf"]),
    "."
  ]},
  {"type": "p", "segments": [
    "Code for America is looking for a talented ", {"b": "Staff Service Designer"},
    " who will ",
    ph("p-multidisciplinary", "work with a multidisciplinary team of designers, researchers, engineers, and policy experts",
       ["ev-delta-pm", "ev-translator", "ev-rampfast"]),
    " to ",
    ph("p-simple-solutions", "analyze problems and create solutions for public services that are simple enough for everyone to use",
       ["ev-pf-legacyux", "ev-eraf", "ev-discovery"]),
    ". As an experienced individual contributor (IC), you'll be responsible for ",
    ph("p-bigger-picture", "seeing the bigger picture of the front-to-back, end-to-end, and digital and non-digital touchpoints",
       ["ev-service-blueprint", "ev-pf-blueprint-global", "ev-site-rebuild"]),
    " that make up the experience of someone interacting with a government program or service in the US. You will be expected to ",
    ph("p-elegant-practical", "identify and advocate for elegant yet practical service design solutions",
       ["ev-exec-alignment", "ev-system-not-symptom", "ev-counseling-restructure"]),
    " to ",
    ph("p-measurable-outcomes", "measurably improve program outcomes",
       ["ev-metrics", "ev-bayer-journey"]),
    " for families while ",
    ph("p-constraints", "minding technology and policy constraints",
       ["ev-ad-constraints", "ev-bayer-journey", "ev-ags-blueprint"]),
    "."
  ]},

  {"type": "h2", "text": "About the role:"},
  {"type": "p", "segments": [
    "As a Staff Service Designer at Code for America, you will play a critical role in transforming public services by ",
    ph("p-human-needs", "designing end-to-end experiences that meet real human needs",
       ["ev-site-rebuild", "ev-discovery", "ev-eraf"]),
    ". You'll ",
    ph("p-multiple-projects", "lead service design efforts across multiple projects",
       ["ev-bayer-flux", "ev-film-producer", "ev-parallel"]),
    " focused on improving complex government systems. You will work within cross-functional teams to ",
    ph("p-current-future", "map current and future states",
       ["ev-pf-blueprint-global", "ev-pf-journey", "ev-service-blueprint"]),
    ", ",
    ph("p-cocreate", "co-create solutions with partners",
       ["ev-facilitation", "ev-counseling-restructure", "ev-delta-pm"]),
    ", and ",
    ph("p-systemic-change", "drive systemic change that improves outcomes",
       ["ev-dryland-scale", "ev-bayer-journey", "ev-counseling-restructure"]),
    " for millions. In this role, you'll also ",
    ph("p-mentor-jr", "mentor junior designers",
       ["ev-mentor", "ev-eq"]),
    ", ",
    ph("p-shape-strategy", "shape strategy with internal and external stakeholders",
       ["ev-exec-alignment", "ev-ags-consulting"]),
    ", and ",
    ph("p-champion-hcd", "champion human-centered design best practices",
       ["ev-facilitation", "ev-adoption"]),
    " across the organization."
  ]},

  {"type": "h2", "text": "In this position you will:"},

  {"type": "h3", "text": "Design Process"},
  {"type": "li", "segments": [
     "Independently ",
     ph("p-lead-execution", "lead service design execution across multiple large and complex projects or workstreams",
        ["ev-bayer-flux", "ev-film-producer", "ev-parallel"]),
     " as an individual contributor."]},
  {"type": "li", "segments": [
     "Demonstrate strong analytical and creative thinking on how to ",
     ph("p-multimodal", "improve the end-to-end, front-to-back, and multi-modal user experience",
        ["ev-site-rebuild", "ev-pf-blueprint-global", "ev-pf-legacyux"]),
     " across your assigned product, project, or portfolio."]},
  {"type": "li", "segments": [
     ph("p-understand-constraints", "Understand the relevant policies, infrastructure, technology, and system constraints",
        ["ev-ad-constraints", "ev-bayer-journey", "ev-ags-blueprint"]),
     " that affect the experience within a given government service."]},
  {"type": "li", "segments": [
     ph("p-gaps-opportunities", "Highlight potential gaps and areas of opportunity for improvement across the whole service",
        ["ev-pf-blueprint-global", "ev-service-blueprint", "ev-eraf"]),
     ", including client, staff, or processes, focusing holistically on all channels of interaction."]},
  {"type": "li", "segments": [
     "Use common service design methods and artifacts to ",
     ph("p-document-interventions", "document proposed service interventions",
        ["ev-writing", "ev-playbooks"]),
     " and clearly communicate your understanding to the team and government partners of current and proposed future state of a service, such as ",
     ph("p-journey-maps", "journey maps", ["ev-pf-journey"]),
     ", ",
     ph("p-service-blueprints", "service blueprints", ["ev-pf-blueprint-global", "ev-pf-blueprint-local"]),
     ", and ",
     ph("p-system-diagrams", "system diagrams and ecosystem maps", ["ev-pf-eraf"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-measure-impact", "Define ways in which a service intervention's impact can be measured",
        ["ev-metrics", "ev-bayer-journey"]),
     " and how impact metrics ladder up to stakeholder goals and user needs."]},
  {"type": "li", "segments": [
     ph("p-user-research", "Participate in planning and carrying out user research activities and synthesizing research findings",
        ["ev-discovery", "ev-counseling-restructure", "ev-pf-usertesting"]),
     ", typically in partnership with qualitative user researchers."]},
  {"type": "li", "segments": [
     ph("p-prototypes", "Create and test design interventions and/or hypotheses by creating low, mid, or high-fidelity prototypes",
        ["ev-pf-personas", "ev-bananas"]),
     ". Use these to ",
     ph("p-iterate", "generate useful feedback and iterate towards the best solution",
        ["ev-agile", "ev-pf-usertesting"]),
     " for people impacted."]},

  {"type": "h3", "text": "Partnership and Collaboration"},
  {"type": "li", "segments": [
     ph("p-partner-disciplines", "Partner closely with individual contributors and managers from other disciplines",
        ["ev-translator", "ev-delta-pm", "ev-rampfast"]),
     " (e.g., engineering, research, product, data science, and program) to find elegant but practical solutions to design challenges."]},
  {"type": "li", "segments": [
     ph("p-workshops", "Design and facilitate collaborative sessions/workshops with internal and external stakeholders",
        ["ev-facilitation"]),
     " to gather input on design directions, identify priority user stories to focus on, and ",
     ph("p-drive-alignment", "drive alignment around strategic design directions",
        ["ev-exec-alignment", "ev-ags-consulting"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-relationships", "Develop and maintain collaborative, professional relationships",
        ["ev-ags-consulting", "ev-delta-pm"]),
     " with government partners, CBOs, and advisory consultants necessary to achieve successful project outcomes."]},
  {"type": "li", "segments": [
     ph("p-presentations", "Deliver presentations to internal and external partners that capture attention",
        ["ev-delta-pm", "ev-exec-alignment"]),
     " and convey key messages succinctly, using ",
     ph("p-storytelling", "storytelling techniques and visual communication",
        ["ev-writing", "ev-facilitation"]),
     " to highlight client and worker experience."]},
  {"type": "li", "segments": [
     "Participate in project or portfolio conversations and ",
     ph("p-sme-input", "provide your input as a service design subject matter expert to inform strategic decisions",
        ["ev-sd-years", "ev-scad", "ev-pf-cdp"]),
     " about project and product direction."]},

  {"type": "h3", "text": "Team Health and Mentorship"},
  {"type": "li", "segments": [
     ph("p-best-practices", "Participate in operational and best-practices initiatives",
        ["ev-writing", "ev-playbooks"]),
     " within the Service Design discipline and the broader User Experience department."]},
  {"type": "li", "segments": [
     ph("p-mentor-staff", "Act as a mentor to support more junior design staff in their work by pairing, coaching, and raising the quality bar",
        ["ev-mentor", "ev-eq"]),
     " of outputs."]},
  {"type": "li", "segments": [
     ph("p-design-feedback", "Deliver constructive critical design feedback",
        ["ev-eq", "ev-facilitation"]),
     " to UX and service design peers."]},
  {"type": "li", "segments": [
     "Serve as a ",
     ph("p-champion-sd", "champion of Service Design across the organization, participating in teaching and learning opportunities, and evangelizing human-centered design",
        ["ev-facilitation", "ev-adoption", "ev-ai-playbook-langs", "ev-pf-prompt"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-thought-leadership", "Contribute to the organization's credibility and thought leadership in design",
        ["ev-writing", "ev-pf-platform-playbook", "ev-pf-genai-playbook"]),
     "."]},

  {"type": "h2", "text": "About you:"},
  {"type": "p", "segments": [
    "This position is a perfect fit for ",
    ph("p-experienced-sd", "an experienced service designer or design strategist",
       ["ev-sd-years", "ev-service-blueprint", "ev-scad"]),
    " who wants to apply their skills to improving large-scale government programs through ",
    ph("p-tech-forward", "technology-forward interventions",
       ["ev-adoption", "ev-pf-personas"]),
    ", while ",
    ph("p-complex-constraints", "thoughtfully considering complex technical, policy, and operational constraints",
       ["ev-ad-constraints", "ev-bayer-journey", "ev-ags-blueprint"]),
    "."
  ]},
  {"type": "li", "segments": [
     ph("p-6years", "6+ years of service design and/or design strategy experience",
        ["ev-sd-years", "ev-service-blueprint"]),
     ", with 2 years at a senior or staff level."]},
  {"type": "li", "segments": [
     "Direct experience working in government services, public policy, civic service design, civic tech, or social impact design in the public sector."]},
  {"type": "li", "segments": [
     ph("p-multichannel", "Demonstrated ability to design, test, implement, and measure complex multi-channel experiences",
        ["ev-site-rebuild", "ev-bayer-journey", "ev-counseling-restructure"]),
     " that include technology systems, business processes, policy constraints, and client-facing artifacts."]},
  {"type": "li", "segments": [
     ph("p-portfolio", "A portfolio of service design work that outlines your design process, deliverables, and impact",
        ["ev-portfolio"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-multiple-initiatives", "Demonstrated ability to manage multiple high-priority initiatives and complex workstreams",
        ["ev-film-producer", "ev-bayer-flux", "ev-parallel"]),
     ", including ",
     ph("p-early-discovery", "early-stage discovery", ["ev-discovery"]),
     " as well as ",
     ph("p-tactical-delivery", "delivery of tactical design improvements to existing processes and technical systems",
        ["ev-pf-legacyux", "ev-agile"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-mentoring", "Experience mentoring designers", ["ev-mentor"]),
     " and ",
     ph("p-value-of-design", "communicating the value of design to stakeholders and cross-functional partners",
        ["ev-exec-alignment", "ev-facilitation"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-travel", "Willingness to travel for research and partner collaboration", ["ev-travel"]),
     " (up to 10% of the time)."]},
  {"type": "li", "segments": [
     ph("p-multidisciplinary-team", "Ability to work collaboratively within a multidisciplinary team",
        ["ev-delta-pm", "ev-translator", "ev-10industries"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-agile-env", "Ability to work in a fast-paced, agile software development environment",
        ["ev-agile", "ev-rampfast"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-mission-passion", "Passion for our mission of making government services better for people who need them",
        ["ev-systems-for-people", "ev-bananas"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-ai-curiosity", "Curiosity about emerging AI tools and a commitment to using them responsibly and effectively",
        ["ev-responsible-ai", "ev-pf-personas", "ev-pf-ai-roadmap"]),
     "."]},
  {"type": "li", "segments": [
     ph("p-mission-commitment", "A deep commitment to Code for America's mission of making government services work well for the people who need them most",
        ["ev-mission-service", "ev-counseling-restructure"]),
     "."]},
]

data = {
  "meta": {
    "candidate": "Ryan Hance",
    "portfolio": "https://www.hance.work/",
    "note": "Pure renderer input. Edit copy here (or in build_data.py). Each highlighted phrase carries the evidence ids that back it; evidence is a shared dictionary."
  },
  "job": {
    "company": "Code for America",
    "role": "Staff Service Designer",
    "employment": "",
    "location": "Remote (in the U.S.)",
    "url": "https://codeforamerica.org/jobs/posting/?gh_jid=8011424",
    "tab_title": "Ryan Hance · Fit Map",
    "candidate_kicker": "Ryan Hance · Fit Map",
    "candidate_lede": "These are selected notes and resume points from Ryan Hance's career experience mapped to the actual Code for America job description.",
    "candidate_stat": "Hover over any underlined phrase and select it to see Ryan's experience related to the ask.",
  },
  "evidence": evidence,
  "jd_prose": jd_prose,
}

out = os.path.join(HERE, "data.json")
with open(out, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# quick self-check: every referenced evidence id exists
ids = set()
for b in jd_prose:
    for seg in b.get("segments", []):
        if isinstance(seg, dict) and "evidence" in seg:
            ids.update(seg["evidence"])
missing = [i for i in ids if i not in evidence]
unused = [k for k in evidence if k not in ids]
print("Wrote", out)
print("phrases:", sum(1 for b in jd_prose for s in b.get("segments", []) if isinstance(s, dict) and "id" in s))
print("evidence items:", len(evidence))
print("missing evidence refs:", missing or "none")
if unused:
    print("unused evidence (fyi):", unused)
