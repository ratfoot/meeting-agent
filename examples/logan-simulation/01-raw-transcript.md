# Raw Meeting Transcript: Dr. Logan Martinez - Discovery Call

**Date:** 2024-02-04
**Duration:** 45 minutes
**Attendees:**
- Dr. Logan Martinez (Principal Investigator, Computational Psychiatry Lab)
- Sarah Chen (HoX.bio, Solutions Architect)
- David (HoX.bio, Account Executive)

---

**[00:00:15]**

David: Hey Logan, can you hear me okay? Let me just, uh, make sure my screen is sharing... there we go. Perfect.

Logan: Yeah, I can see it now. Thanks for making time today. I know we're all busy.

Sarah: Of course! So Logan, before we dive in, maybe you could give us some context about what's driving this conversation? What made you reach out?

Logan: Right, yeah. So, um, I run a computational psychiatry lab. We're trying to build machine learning models for treatment response prediction in depression. The science is actually going really well—we've got promising preliminary results. But honestly? I'm spending way more of my budget on data wrangling than on actual science.

David: Got it. When you say data wrangling, what does that actually look like day to day?

Logan: Oh god, where do I start. [laughs] So we pull data from multiple sources—UK Biobank, some stuff from NCBI GEO, we've got collaborators in the Netherlands using the Snellius supercomputer. And every single source has its own, you know, its own format, its own coordinate system, its own access requirements.

Sarah: That sounds painful. Can you give us a specific example?

Logan: Sure. So UK Biobank, right? Amazing resource. But it took us EIGHT MONTHS just to get the Data Use Agreement approved. Eight months of my postdoc's time doing paperwork instead of science. [!] And even after we got access, we can't actually move the data. It's stuck in their walled garden. So now we're paying egress fees every time we want to run an experiment.

David: Egress fees?

Logan: Yeah, cloud egress. Every time we pull data out to our compute environment, we're paying. I did the math last quarter—we spent $47,000 just moving files around. That's almost a postdoc salary. [$]

Sarah: Wow. And what about the normalization piece you mentioned?

Logan: That's the worst part, honestly. So we've got genomic data in hg19 coordinates from one source, hg38 from another. Clinical phenotypes have different column names. Timestamps are formatted differently. My bioinformatician—brilliant guy, could be training models—spends probably 60% of his time just... munging. Cleaning. Reformatting. It's digital janitorial work. [!]

David: 60%? That's significant.

Logan: It's insane. And I can't even blame him—the data comes in messy. We have no choice. But when I write my grant renewals, I have to justify why my "machine learning lab" is spending most of its compute budget on storage and ETL pipelines instead of, you know, actual machine learning.

Sarah: Have you tried building internal tooling to automate some of this?

Logan: We tried. Twice, actually. The problem is every time we pivot to a new methodology or add a new data modality, we have to rebuild everything. There's no central warehouse. No versioning system that actually works across modalities. We're basically recreating the wheel every six months. [!]

David: What's the opportunity cost there? Like, if your team wasn't doing all this data work, what would they be doing instead?

Logan: [sighs] We'd be publishing. We'd be training models. We have this really promising graph neural network architecture for predicting lithium response, but we've been sitting on it for four months because we can't get the multi-modal data aligned fast enough. My competitors at Stanford, they published something similar last month. We had the idea first. [$]

Sarah: That must be frustrating.

Logan: Frustrating doesn't cover it. I'm a PI. My job is to make discoveries. Instead I'm a... data janitor with a PhD.

David: So if I'm hearing you right, there are really four problems here: the access delays with DUAs, the egress costs, the normalization overhead, and the lack of a unified warehouse for versioning and iteration?

Logan: Yes. Exactly. That's the "Data Harmonization Tax" I keep talking about in my lab meetings.

Sarah: Love that framing. So what would success look like for you? If we could wave a magic wand?

Logan: Honestly? I want to redirect that 60% back to science. I want my bioinformatician training models, not cleaning CSVs. I want to stop paying cloud egress to move my own data around. And I want a system where, when I pivot to a new modality—say we add EEG data next year—I don't have to rebuild my entire pipeline.

David: [?] Who else would need to be involved in evaluating something like this? Is it just your lab, or does this need institutional buy-in?

Logan: Good question. For a pilot, it's just me—I have discretionary grant funds. But if we wanted to scale this across the department, I'd need to get Dr. Patel involved. She's the department chair. And IT Security would need to sign off on anything touching protected health data.

Sarah: Makes sense. What's the first dataset you'd want to load if we did a pilot?

Logan: The UK Biobank psychiatric cohort. About 15,000 subjects with genomic and phenotypic data. If you could show me that ingestion-to-analysis goes from two weeks to, I don't know, four hours? That would be the proof point.

David: That's really helpful. [*] I'll send over a technical spec for how our warehouse handles Biobank data specifically. And maybe we can set up a follow-up with your bioinformatician to walk through the API?

Logan: That would be great. His name is Marcus—I'll loop him in.

Sarah: [*] And I'll put together a quick ROI model based on the numbers you shared—the $47K egress, the 60% time allocation. Would be good to have that documented when you talk to Dr. Patel.

Logan: Perfect. I have a grant renewal deadline in 90 days, so if we could move quickly on this, that would really help my planning.

David: Understood. Let's aim to have the technical deep-dive next week, and we can reconvene with a proposal within two weeks. Sound good?

Logan: Sounds great. Thanks for actually listening. Most vendors just want to demo features. You actually asked about my problems.

David: That's the job. Talk soon, Logan.

Logan: Take care.

---
**[END TRANSCRIPT]**
