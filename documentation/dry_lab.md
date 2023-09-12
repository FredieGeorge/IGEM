[5/5, 1:27 AM] Aman Sahoo: 
Dry Lab, can you guys tell me what exactly you will be modelling as we go forward? ELI5 please

[5/5, 10:26 AM] Mrigank Pawagi:
    I am working on a detailed list of things we could do. For now, we will be working on molecular docking to show the binding of IL8 with our antibody. 

[5/6, 12:35 PM] Mrigank Pawagi
Dry Lab Check out this repository about scFv Structure Modelling. In particular, read the README file.
https://github.com/iGEMIISc/scFv-Modelling

Today, we will be focusing on manual homology modelling using Modeller. After a short discussion on how to get started, we will try to directly get to modelling using the templates I have outlined in the README. 

The purpose for generating models through different methodologies is preventing gross errors. Moreover, I came across a technique for combining multiple models by taking out the best parts from each of them. We can use this to refine our model. I will talk about this too in today's session. 

I was able to use modeller on our templates. It turned out that chain C of 6Y6C is the best fit. You can find all relevant code and other files in the /modeller folder.
Feel free to post any questions on this channel. 

[5/7, 12:33 AM] Sheersh Sen
    Dry Lab Today's Meeting Summary. I wasn't really there so I definitely missed out some parts. Kindly add to the document as needed.[Document](/files/Homology.docx)

[5/4, 10:16 AM] Mrigank Pawagi
Basic Homology and Docking Tutorials
    (Dry Lab) For those of you who are interested in learning about homology and docking, I am planning to keep a discussion session over the weekend. Does Saturday afternoon (roughly 2-4:30 PM) work? We can keep another session later if we aren't able to cover everything planned. We will meet in the math department. Please react to this message if you plan to come. Bring your laptops along. 
	[5/4, 10:19 AM] Yukta Subramanian
	    Do you plan to keep it in hybrid mode?
	[5/4, 10:22 AM] Mrigank Pawagi
	    We can try. I was thinking that Varivashya and I could document the session(s) to create guides which we can later put on our wiki (does this make sense, Sheersh?). Nevertheless, one of us will make notes which you can refer to later. 
	[5/4, 10:39 AM] Sheersh Sen
	    yeah that works. i'll try to help with the documentation thingie too
	[5/6, 2:28 PM] Mrigank Pawagi
	    https://salilab.org/modeller/tutorial/basic.html
	[5/6, 10:14 PM] Mrigank Pawagi
	    Sheersh please share your notes whenever you're free. 
	[5/6, 10:15 PM] Sheersh Sen
	    yup, in a minute. i wanted to discuss some things on whatsapp first
	[5/9, 7:07 PM] Aryaman Bhutani
	    Hi, if you guys want a docking tutorial do let me know. I worked a lot with Autodock Vina and can guide you on the same. While at first the tutorials etc may appear easy to approach, they can have many nuances. 
	[5/9, 7:09 PM] Aryaman Bhutani
	    Also you can approach me for BioPhysics related aspects of modelling. I also worked a bit on Molecular Dynamics simulations, and while I am not an expert at them (Megha probably has worked with them more), I can point you to resources that you will find easy to follow and absorb.
##GitHub Organization and Kanban Board
[5/10, 10:59 AM] Mrigank Pawagi:
(Dry Lab) Please share your GitHub usernames so that I can add you all as collaborators in the iGEM-IISc GitHub organization. Once that is done, you can view the Tasks view at https://github.com/orgs/iGEMIISc/projects/1/views/1. We will be using this board to keep track of our tasks. I will put up more things to do within a day or two. 

Thanks to Hemanya for pointing out the need for better task management.

[5/12, 12:35 PM] Aditya Kamath Ammembal
    Dry Lab I have uploaded the entire sequence with the tags and stuff. Sorry for any inconvenience caused. i will also add the aptide sequence in here.
	[ab sequence with tags and stuff.docx](Documents/IGEM/documentation/filesab_sequence_with_tags_and_stuff.docx)

[5/22, 12:14 AM] Mrigank Pawagi
##Updated scFv Models
I have added updated models from AlphaFold and SWISS-MODEL to the repository. Would somebody like to document them in the README file? Just include rank-1 models from AlphaFold (both with and without templates). Also, include relevant data about quality of each model. Images of the models would also look good. Note that the rank-1 AlphaFold models were relaxed by AMBER; this should also be mentioned. 

Additionally, if you are interested, you can look at the modeller directory in the "without histag" directory and rerun the scripts for the complete sequence. Our top template, 6y6c is the best template for the complete sequence too. 

Let me know if you need any help.

[5/25, 1:27 PM] Aditya Kamath Ammembal
    Dry Lab I ran another run of the Signal peptide with the antibody sequence through SignalP6.0 instead of SignalP 5.0, which I had previously used. The results are still excellent and indicative of our using the CD33 peptide. The zip file of all data is uploaded under files. 
[5/25, 2:54 PM] Mrigank Pawagi
    	Perfect! 
#Pharmacokinetics
    
[5/10, 10:08 AM] Mrigank Pawagi
Dry Lab Please use this thread to share any interesting ideas or resources you come across while reading through literature on pharmacokinetics. For starting with basic concepts in pharmacokinetics, you can check out the attached textbook. You can also try this NPTEL course: https://nptel.ac.in/courses/102108077 (by Prof. Rachit).

[Robin Southwood, Virginia H. Fleming, Gary Huckaby - Concepts in Clinical Pharmacokinetics-American Society of Health-System Pharmacists (2018)](https://books.google.com/books/about/Concepts_in_Clinical_Pharmacokinetics.html?id=U2JyDwAAQBAJ)

[5/20, 12:26 PM] Mrigank Pawagi
    https://www.frontiersin.org/articles/10.3389/frph.2021.699133/full

[5/27, 12:46 AM] Anwesha Malla
    Raloxifene-HCl is a non-steroidal drug having antiestrogenic effects on the endometrium. This paper talks about how SLNs have been used to transport the drug. Since the LNP being used in our project will also work in a similar environment, i.e. the endometrium, pharmacokinetic data for SLNs used in this might be useful for us.
[RL-HCl.pdf](Documents/IGEM/documentation/filesRL-HCL.pdf)

[5/27, 1:50 AM] Anwesha Malla:
    Docetaxel is an anti cancer agent. LNPs have been used for its delivery. The relevant portion for us in this paper is under in vitro NP characteristics.
[docetaxel-loaded-plga-and-plga-peg-nanoparticles-for-intrave_012717.pdf](Documents/IGEM/documentation/filesdocetaxel-loaded-plga-and-plga-peg-nanoparticles-for-intrave_012717.pdf)

[5/27, 2:02 AM] Anwesha Malla:
Dry Lab, Aditya Kamath Ammembal This paper is on mRNA-lipid nanoparticle COVID-19 vaccines. Table 1 is important.
[Covid vaccines by Pfizer and Moderna.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Covid vaccines by Pfizer and Moderna.pdf)

[5/27, 2:23 AM] Anwesha Malla:
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9238147/
[5/28, 9:54 PM] Tarushri N S
    Resveratrol - Inhibits the release of cytokines (TNF-alpha, IL-6, IL-8, VEGF, MCP-1) and the production of reactive oxygen species in monocytes, macrophages, and lymphocytes. Section 8.5 of the following paper contains the details related to action of resveratrol.
(1 liked)[Novel drug targets with traditional herbal medicines for overcoming Endometriosis.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Novel drug targets with traditional herbal medicines for overcoming Endometriosis.pdf)

[5/28, 10:06 PM] Tarushri N S:
    
The following paper is about how resveratrol enhances mRNA and siRNA LNPs Primary Chronic Lymphocytic Leukemia (CLL) cell transfection... 2.2- LNP preparation and Characterisation... 2.5- LNP uptake experiment... 3.1- Physiochemical and structural characterisation of LNPs... 3.3-Resveratrol enhances mRNA LNP transfection into Primary CLL... 4.-DISCUSSION. Note that this paper is about CLL cells and not endometriotic cells but still we may get some useful info about LNPs... Also check out some important papers relevant to LNPs under references (12.Lipid nanoparticles for short Interfering RNA delivery, 15.Advances in lipid nanoparticles for siRNA delivery, 44.The role of surface chemistry in serum protein corona-mediated cellular delivery and gene silencing with lipid nanoparticles, 46.Linkage between endosomal escape of LNP-mRNA and loading into EVs for transport to other cells, 50.Transferrin-targeted, resveratrol-loaded liposomes for the treatment of glioblastoma.) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7355647/


[5/29, 7:17 AM] Aditya Kamath Ammembal
    Dry Lab I would like all of you working on pharmacokinetics to go through the following link: it seems very helpful.  https://2012.igem.org/Team:Slovenia/ModelingPK  
[6/1, 8:29 AM] Sheersh Sen
    Also, this is a good time for interested peeps to start going through SimBiology Documentation (SimBiology is just a bunch of apps for modelling, computation, simulation etc. that is relevant for us). There are tons of video tutorials on using the thing for iGEM, and you can just google them. I'll add a link to documentation for us to get started.
https://in.mathworks.com/help/simbio/
[6/1, 12:00 PM] Mrigank Pawagi
    We will almost certainly require MATLAB, although SimBiology may or may not be required. Nevertheless, its a good skill to have and I would also encourage everybody to check it out if possible. 
[6/1, 9:43 PM] Sheersh Sen
    Dry Lab Brief meeting minutes[minutes]
[6/5, 4:22 PM] Sohaan Kumar Pattanayak:
    
Dry Lab Paper 1 is about the working of generalized mRNA-LNP delivery systems in mRNA therapy as of now, with considerations in specific diseases and the PK-PD analysis ( October 2022: comprehensive enough for our need); Paper 2 is an example of LNP-mRNA delivery by intraperitoneal administration(Jan 2023).

[mRNA-LNP delivery systems.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Research Papers/mRNA-LNP delivery systems.pdf)[LNP delivery-intraperitoneal administration.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Research Papers/LNP delivery-intraperitoneal administration.pdf)
[6/19, 10:17 AM] Anwesha Malla:
Dry Lab Here are some papers regarding harmful concentrations of IL8.                                                                                                        Detailed information about the concentrations of IL8 is given in the results section of the pdf titled Interleukin-8 concentration in peritoneal fluid and table 1 of the other pdf, which mentions concentrations of IL8 in the various stages of endometriosis.


[Interleukin-8_concentration_in_peritoneal_fluid_of.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Interleukin-8_concentration_in_peritoneal_fluid_of.pdf)[1-s2.0-S0015028216575062-main.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/1-s2.0-S0015028216575062-main.pdf)
#scFv modelling appears to be complete
[6/21, 1:39 AM] Mrigank Pawagi
    Dry Lab
Please check the repository (https://github.com/iGEMIISc/scFv-Modelling), particularly the README. I have (tentatively) completed the documentation for our modelling, and was also able to run some simple comparative analysis as previously planned. I have decided to not go with Nisha's advice of picking a model based on its docking efficiency because that will be logically circular, and will bias our docking results. I request the following from all of you.



	
Please read the documentation and let me know if anything needs to be clarified.
	
Check for any errors/ambiguities in the documentation and make modifications or additions (by making a "pull request" on GitHub; I will help you with this if you are new to git)
	
Create slides from the README! Sheersh previously suggested that we should be making everything we do presentable and now that we have some content to show, we can start doing this. If you are interested in helping out here, please contact Sheersh and work with him. As always, feel free to ask me personally or ask here on the group for any clarifications.

We can discuss this in our meeting (in ~15.5 hours).

#Meeting + Goal Setting
[6/17, 11:51 AM] Mrigank Pawagi
    (Dry Lab) We will meet online, this Wednesday. Please let me know what time works for you in the replies' section. Till then, we have the following broad tasks to work on. I will suggest that we broadly skim all of them for a few days, and maybe continue what we were doing before examinations (for example, if you were reviewing MATLAB or some particular set of papers, get through it in this time). 



	
* Modelling and documentation

* Setting up docking

* Reading for pharmacokinetics to answer questions like: 
		
			* How much IL8 is too much? What concentration do we need for reduced/no inflammation?
					
			* What removal efficiency does our anti-IL8 scfv have?
					
			* What is the efficiency of production and ejection of scfv from endometrial cells?
					
			* What is the translation efficiency of our mRNA?
					
			* What is the efficiency with which LNPs are taken up by cells?
					
			* What concentration of LNPs do we require in the peritonium?
					
			* What is the general behavior of LNPs with respect to pharamokinetics? 
				
	

Feel free to add on to these. 

[6/19, 11:45 AM] Aditya Kamath Ammembal
    Dry Lab Please find attached the sequence of the gene with the UTRs we are using, as I was asked for. I have also uploaded the .dna file here, which can only be opened on Snapgene viewer. If you don't have it, you can still get a one-month free trial for the same on snap gene's website. 
(1 liked)[O-IL8-15 sequence word.docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/O-IL8-15 sequence word.docx)[GS-mK-100A-BspQI-GOI (1) (1).dna] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/GS-mK-100A-BspQI-GOI (1) (1).dna)
[6/21, 3:18 AM] Mrigank Pawagi
    Do you want the sequence to be validated for stability? (or some other kind of analysis?)
[6/21, 4:07 AM] Aditya Kamath Ammembal
    I put it up because @anwesha asked me for the sequences. Didn't put it up for any specific task I wanted done. 
[6/21, 10:29 AM] Mrigank Pawagi
    OK, will discuss with her in the meeting.
[6/21, 1:17 PM] Anwesha Malla
    I asked for it to see if I could work on finding the translation efficiency of the mRNA(as you mentioned in the 4th task).
[6/21, 7:08 PM] Sheersh Sen
    Dry Lab Rough meeting minutes and weekend goals have been uploaded. Please add in anything I might've missed.
(1 liked)[DryLab5, 21062023.docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Summaries/DryLab5, 21062023.docx)
[6/24, 10:32 PM] Sheersh Sen
    Dry Lab So I spent some time going through the mRNA-LNP Delivery System paper uploaded. I'm around 10 pages into the paper (out of 23) but so far it has been a very useful resources. I have uploaded a file named 'Homework' in the mRNA-LNP folder with relevant points I've found so far. A summary follows:

	
1. So the LNP enters the cytosol through cell membrane by endocytosis. 
	
2. I've uploaded a paper on the stability of mRNA loaded LNPs. They're pretty stable, so allow delivery into cells.
	
3. Release of mRNA into cytosol is by breaking down of endosome.
	
4. There's very low release of mRNA from LNP into cytosol (only 2-3%). The entire process has been visualized in vivo.
	
5. Different helper lipids give different endosomal release rates (DOPE is good, which DSPC inhibits endosomal release of mRNA)
	
6. The paper also deals with immunogenicity. The lipids do cause an increase in anti-PEG antibodies. The actual mRNA structure doesn't matter for the LNP immunogenicity.
	
7. Another paper deals with a comparative study of various mRNA delivery methods and shows why LNP methods are more efficient.

8. I'll keep updating the docx file and add more relevant papers over time.
(1 liked)[Homework.docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/mRNA-LNP Delivery Systems/Homework.docx)
[6/25, 12:05 AM] Anwesha Malla
    
Dry Lab I have uploaded a few papers to the folder titled "Pharmacokinetics of lnps data presentation". We can refer to those papers to understand what relevant questions we can answer, for example, the efficiency of drug delivery in the presence of lnps. It would also be great if we can come up with a way for pharmacokinetic analysis and biodistribution as done in the paper on docetaxel.
[6/25, 12:27 AM] Anwesha Malla
    Dry Lab I have uploaded a paper to the folder titled "Immunogenicity and other properties of lnps" that deals mainly with the immunogenicity of lnps . It also has many references which might be useful for studying about the pharmacokinetics of lnps. 

[6/25 2:08 AM] Mrigank Pawagi
### On Molecular Docking

I figured out that our antibody-antigen was computationally too demanding for Autodock, which is generally used with small ligands. Our "ligand" (IL8) has somewhere around 2000 atoms! I turned to several web servers, including Patchdock (+Firedock), DockRMSD, ClusPro, ZDOCK and **GRAMM**. Out of these, GRAMM worked for us and provided seemingly good results (check README of [repository](https://github.com/iGEMIISc/Docking-scFv-IL8 "https://github.com/igemiisc/docking-scfv-il8") for GIFs). GRAMM is developed by University of Kansas. It does not give "real" units of energy but rather something called a shape-complementarity score. I am in touch with a PhD student from the research group maintaining GRAMM and I have requested him to share some data for us to train a regression model for determining interaction energy from GRAMM's score. This data _might_ be useful for determining the binding efficiency of our scFv with IL8.

**To do:** Figure out which of the two dockings is more effective by working out the real energies for both the methods (Free and Template-based).

### On Biomarkers

Anwesha has done a good job at collecting literature on biomarkers. It seems that besides IL8, there do exist several other chemical biomarkers, but significance of these is not very well established. 

-   (Side-exploration) What is the method for determining some of the most important of these biomarkers? Blood test?
-   One paper that takes this theoretical approach to something more concrete is [this](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.13040 "https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.13040"). They relate bone mineral density with endometriosis through a long chain of relations (calcium homeostasis, elgolix, estradiol). You can also check [this paper](https://ascpt.onlinelibrary.wiley.com/doi/full/10.1038/psp.2012.15 "https://ascpt.onlinelibrary.wiley.com/doi/full/10.1038/psp.2012.15"), although this has much more less-relevant information.
-   [This paper](https://ascpt.onlinelibrary.wiley.com/doi/full/10.1038/psp.2012.10 "https://ascpt.onlinelibrary.wiley.com/doi/full/10.1038/psp.2012.10") extends the above model to relate estrogen levels with endometriotic-pain (for regulating drug dosage \[it seems excess estrogen causes bone mineral density loss\]). 
-   **Our goal**: We want to describe, as part of our model, a way to regulate our drug dosage (and observe its action). 
    -   The above papers may not directly be very useful, since they are relating a physiological phenomenon (BMD change or pain) with factors resulting from hormonal-drug usage, which we are not doing.  
    -   Since our drug finally targets IL8, we need to be able to determine IL8 concentration.
    -   One idea that might work is that we can take the IL8 concentration vs active lesion score data from [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7573391/ "https://www.ncbi.nlm.nih.gov/pmc/articles/pmc7573391/") and relate it with the lesion score vs endometriotic stage data from [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6257623/ "https://www.ncbi.nlm.nih.gov/pmc/articles/pmc6257623/") and the endometriotic stage (and other factors) vs pain data from [this paper](https://www.sciencedirect.com/science/article/abs/pii/S1074380499800061 "https://www.sciencedirect.com/science/article/abs/pii/s1074380499800061"). The broad question then becomes "_Can we find a relation between IL8 and pain?_" (Note that some papers have mentioned that there might be disparity in data related to pain; can we think of an alternative?)
    -   Besides preventing underdosage, regulation may also be valuable if overdosage of LNPs poses a risk of some kind of toxicity. _Is this the case?_

**To Do:** Continue on these leads and collate data. Once that is done, models and other things can be worked out. 

(Extra & low-priority) I found [this paper](https://www.nature.com/articles/s41598-018-22749-0 "https://www.nature.com/articles/s41598-018-22749-0") about using data from Organ-on-Chip systems (which we would be using as well!) to predict _in vivo_ QSP models.

### On Translation Efficiency

Sheersh has found some _in vivo_ parameters that can determine translation efficiency. Please discuss this with Yukta or Mayank to see if we will be doing those experiments, and update here.

-   [This paper](https://www.pnas.org/doi/10.1073/pnas.0909910107 "https://www.pnas.org/doi/10.1073/pnas.0909910107") talks about the effect of codon bias (multiple codons can code for the same protein) and folding energy (of RNA) on translation efficiency. Can we crunch any hard numbers out of this study?
-   [This](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016036 "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016036") is a much more involved paper. It discusses many more factors.
-   You may also like to check out [RiboDiff](https://public.bmi.inf.ethz.ch/user/zhongy/RiboDiff/index.html "https://public.bmi.inf.ethz.ch/user/zhongy/ribodiff/index.html").

**To do:** Continue on these leads.

### On PK of LNPs

Sheersh and Anwesha have done a great job at getting hold of relevant information. Could you individually/together summarize your relevant findings and present this week in a short meeting? This is a loaded topic and it would be helpful for everyone to get up to speed in this respect.

### On ELISA

I have been reading up on ELISA, and saw through the paper Aditya sent on General. I have got some insight, but despite going through multiple have been unable to find a  correlation between ELISA data and "real" (_in vivo_, so to speak) data. Aditya, could you point me to the dataset you mentioned you had seen? 

### More?

Sanika, Tarushri, Varivashya, Saahiti, Sanjana, Hemanya: Please share any updates in the replies.

-   If you are stuck, feel free to report whatever you have found whether or not you think it is relevant.
-   If you need help understanding something, feel free to ask and discuss here or in-person or via DM.
-   If you are busy, share a little report on your work with directions on how to carry it forward. Somebody else can continue it while you're away.

### Next?

Let us meet next Sunday, preferably (for me ![😅](https://statics.teams.cdn.office.net/evergreen-assets/personal-expressions/v2/assets/emoticons/sweatgrinning/default/20_f.png?v=v29?v=5)) at night. 
[6/25, 8:40 AM] Sheersh Sen
    I'll work with Anwesha Malla on the PK of LNPs part and sure, we'll present our findings. And I'll continue with the Translation Efficiency part. I also plan to look into protein release efficiency from transfected cells this week. That's it for now! 
[6/21, 11:03 PM] Anwesha Malla
    
Dry Lab Mrigank Pawagi I searched for biomarkers for endometriosis. As of now, no specific biomarkers of endometriosis have been identified (laparoscopy and other methods are used to diagnose it) and none of the studies show very conclusive evidence of an increase in a potential biomarker in endometriosis.  I have attached two pdfs which I felt might be relevant as it has data of the studies carried out to determine if we can have a biomarker for endometriosis. The pdf titled "Endometriosis epidemiology .."has biomarkers under section 10., and the pdf titled "Peripheral biomarkers for endometriosis" has data about the various potential biomarkers like IL8 and IL6 from page 657.

[Peripheral biomarkers for endometriosis.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Peripheral biomarkers for endometriosis.pdf)
[6/23, 12:20 PM] Mrigank Pawagi
    Thanks, let me check this out today. 
[6/25, 12:52 PM] Anwesha Malla
    Dry Lab I have uploaded a book called "Biomarkers for Endometriosis State of the Art" to the folder "Biomarkers for endometriosis". It deals with a number of biomarkers and endometriosis in general in great detail. 
[6/26, 9:02 AM] Aditya Kamath Ammembal
    Looks like I won't be able to get the required antibody on time, so I'll be investigating a different method of testing binding specificity and affinity. 
Also, I found some really useful stuff. Namely, the mechanism of uptake of APTEDB-conjugated NPs is probably Caveolae-mediated endocytosis!! https://www.mechanobio.info/what-is-the-plasma-membrane/what-is-membrane-trafficking/what-is-caveolar-endocytosis/

Further, I also found a paper discussing the distribution and accumulation of APT-EDB conjugated NPs in tumour tissue after an IV. 
I dunno if this is exactly what you guys want, but I thought it may be handy.

As for the exact binding eff of the antibody, I will give the data to you. It is not in the paper I sent in general, and I thought i had shared that one too.
[6/26, 9:04 AM] Aditya Kamath Ammembal
    Dry Lab I will upload a quick summary of the endocytosis thingie by the end of today if you would like me to.
[6/26, 9:05 AM] Aditya Kamath Ammembal
    Dry Lab Whoops! forgot the link to the paper i was talking about https://doi.org/10.1016/j.biomaterials.2014.06.022
[6/26, 10:14 AM] Mrigank Pawagi
    Thanks a lot for these resources. We'll check them out and get back.
[6/28, 4:01 PM] Aditya Kamath Ammembal
    Dry Lab Sorry I forgot to mention, but I've located a Surface Plasmon Resonance facility in the MBU, and we'll probably be able to access it, so we'll have good affinity data when we purify the antibody. 
(1 liked)​[6/28, 4:11 PM] Aditya Kamath Ammembal
    Dry Lab https://www.thesgc.org/biological-probes/il-8 this has EVERYTHING about the antibody and the antigen
[6/30, 1:35 AM] Sheersh Sen
    Dry Lab Here's all I've got so far on LNP PK/PD. The document's pretty self explanatory, so please do go through it. You can figure out ways to progress further from it, I guess :")
[DryLabUpdates.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/mRNA-LNP Delivery Systems/DryLabUpdates.pdf)
[6/24, 10:35 PM] Sheersh Sen
    Dry Lab Also, regarding the mRNA translation efficiency, there's a paper containing code (in Python and R) to analyse certain in vivo observations that gives us a measure of the translation efficiency. However, that might needs some input from the Wet Lab team as well. It involves something called ORFs (Open Reading Frames). Will upload relevant papers soon.
(2 liked)​[6/25, 7:59 PM] Sanika Amol Borade
    



Dry Lab I have uploaded some papers on translation efficiency. (One of them is link in a word file since I could not find the pdf).

I’ve read one of them completely and it talks about using oligonucleotides to increase the translation efficiency. This isn’t that relevant to the questions at hand but I'll put up a short summary soon.

I’m also reading the ORF paper you’ve put up. (ORF is basically just a sequence of codons to be read by the ribosome, it’s explained well here) 



(1 liked)Edited​[6/30, 1:38 AM] Sheersh Sen
    Yeah I printed the link in the docx into a PDF and uploaded it. (I erroneously named it "mrnaeff" when it's not exactly about that lol) 
[mrnaeff.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/mRNA-LNP Delivery Systems/mrnaeff.pdf)
[7/4, 12:56 AM] Anwesha Malla
    Dry Lab Here's what I collected for PK and PD of LNPs. I will upload more papers soon. Mrigank Pawagi, the link to the site containing the CSV file is given, in case you or anyone else wants to check it out tonight.
(1 liked)[PK and PD of LNPS.docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/PK and PD of LNPS.docx)

[7/4, 2:28 PM] Anwesha Malla
    General,Aditya Kamath Ammembal Here is the document with the link to the papers which show why we want to target IL-8 to find a solution for endometriosis. I think I have put all the pdfs in the project proposal relevant to this and have added some myself. 
[Reasons for targetting IL-8 .docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Reasons for targetting IL-8 .docx)​[7/4, 8:41 PM] Aditya Kamath Ammembal
    Anwesha Malla, Thanks! As promised, I will collate all the evidence I can and get back to you, hopefully by the end of this week
​[7/13, 12:24 PM] Anwesha Malla
    I added another link here. Aditya Kamath Ammembal, should I put all the links in this document in the other document shared in the iGEM confirmed group, earlier?
​[7/13, 12:25 PM] Aditya Kamath Ammembal
    Anwesha Malla, Please do, it would make everything easier for those collating evidence
(1 liked)​[7/13, 12:26 PM] Aditya Kamath Ammembal
    also, iGEM 2023 could I please have an update on the evidence collation thingie?
[7/14, 2:25 AM] Mrigank PawagiDocking of scFv with IL8 is complete!
    (Dry Lab) Our work on docking is tentatively done! I was able to determine binding affinity using PRODIGY. I have credited the guy from UoK in the README. Sheersh, please make a note of that for HP. Most importantly, I request all of you to thoroughly read the documentation and suggest any required improvements. https://github.com/iGEMIISc/Docking-scFv-IL8/
[7/13, 5:26 PM] Anwesha Malla
    
Dry Lab Here is the Word document with links to the papers that are useful for relating IL-8 concentrations with active lesions score. However, I have some doubts-There is no mention of active lesion score of 3 in the 4-point scale. Can Aditya Kamath Ammembal, Mrigank Pawagi , or anyone else please help me understand this? Secondly, I haven't found a paper with very well-defined concentrations of IL-8 in the various stages of endometriosis. One of the documents here deals with concentrations, but the stages have been clubbed together, like stages 1,2 and stage 3,4. It will be helpful if any of you too search for the data on the concentration of IL-8 in various stages.
[Relating il-8 levels with active lesion score.docx] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/Relating il-8 levels with active lesion score.docx)​[7/14, 11:47 AM] Mrigank Pawagi
    Wonderful! This goes in the right direction. Let us discuss this in a meeting this weekend. We can do some interesting things with this. We will discuss how we can fill in gaps in the data.
Edited​[7/15, 1:05 AM] Aditya Kamath Ammembal
    Hi Anwesha Malla; sorry for getting back to you so late. For your clarification about the whole stage 3-4 confusion, I saw what you were referring to. In the rASRM classification of endometriosis, you will see that the lesion score is NOT the same as the stage of endometriosis. We add the scores to get a total, based on which we decide the stage. I hope this answers your question? 
​[7/15, 1:06 AM] Aditya Kamath Ammembal
    They are simply correlating the lesion score to the IL8 concentration
​[7/15, 1:07 AM] Aditya Kamath Ammembal
    Also, the lesion score can go to, like, 20 or something, if I'm not wrong...
​[7/15, 8:06 AM] Anwesha Malla
    Thanks for the reply Aditya Kamath Ammembal . I was asking about the scoring of individual lesions, which according to a paper is as attached in the screenshot. Here there's no mention of score 3. Another paper I went through had same information. So I wanted to confirm if a score of 3 is not assigned to individual lesions.
[20230715_080225.jpg] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared%20Documents/Dry%20Lab/20230715_080225.jpg)​[7/15, 4:44 PM] Aditya Kamath Ammembal
    Yes, the lesion score is arbitrary, as mentioned in the paper in which it was introduced. This is why there is no 3...... To make things add up and fall in a range, most probably. 
​[7/15, 4:44 PM] Aditya Kamath Ammembal
    Anwesha Malla, this is in fact why, newer systems are trying to replace it!
​[7/15, 5:09 PM] Anwesha Malla
    Thanks
[7/31, 12:12 PM] Sanjana D S
    Is there a plan to simulate the structure of LNP with mRNA?
(1 liked)[lnp formulation prediction.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/lnp formulation prediction.pdf)​[7/31, 12:14 PM] Sanjana D S
    I have marked 2 paragraphs, the info after that might be helpful in modeling the lnp with the lipid formultion chosen
​[7/31, 3:02 PM] Mrigank Pawagi
    Thanks for sharing! Let's discuss this today evening.
[7/31, 9:41 PM] Sanjana D S
    Today’s mentions in the meeting
Please add to it if I missed something
[7/31, 10:07 PM] Sanjana D S
    These are some Wikis which have good PD, PK models relevant to us I feel.
(1 liked)[WIKI SEARCH.odt] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared%20Documents/Dry%20Lab/WIKI%20SEARCH.odt)
[8/2, 5:11 PM] Sanjana D S
    Chapter 4 of this Journal has description of many pharmacokinetics models. So does chpt 5.
Some of the modelling softwares mentioned in chpt 4 are
- Simcyp
- PKSIM( www.simcyp.com )
-CLOEPK( www.systemsnoilogy.com/products/pk-sim.html )
- ADMEWORKS DDI Simulator ( http://www.fqs.pl/chemistry_materials_life_science/products/ddi_simulator )
Chpt 4, 5, 6, 7 seem relevant. I have started reading them, yet to be finished.
(1 liked)[Patel 2022, Pharmacokinetics and Pharmacodynamics of Nanoparticulate Drug Delivery Systems.pdf]

[8/2, 10:14 PM] Sheersh Sen
    Dry Lab I've uploaded 2 papers in the PKPDMathModel folder. One exclusively deals with siRNA-LNPs and the other works on a mRNA-LNP vaccine model, like the CoVID one to predict immunological timescales. Both come up with purely mathematical models that require a bit of input from in vitro tests to deal with the entire PK business. I'll be going through them a bit more thoroughly and maaaybbeeee contact authors for some HP purposes grinningfacewithsmilingeyes
[8/6, 7:25 PM] Mrigank PawagiOn mRNA Optimization
    I was able to install all dependencies for Ribotree but there was some issue in running it on the example sequences. I wanted to transfer that repository to my local system but unfortunately, I have carelessly exhausted my storage and have been locked out of the online virtual machine till 15th August sad. I will get back to it then, because I really don't want to redo all of that. Sorry for the delay! We can try some other fully automated web servers for mRNA optimization in the mean time though. (Aditya)

I will update this post when this thing goes forward. 
​[8/6, 7:36 PM] Aditya Kamath Ammembal
    Ah, no probs! Is it possible to continue the work on another machine? Idk. If not, it's perfectly ok, we can be delayed for some time.
​[8/6, 8:15 PM] Mrigank Pawagi
    Yes, I can start over again. Should be easier this time though. I had a script with all the manual fixes in my (now) locked codespace. 
​[8/6, 8:53 PM] Aditya Kamath Ammembal
    Oh, cool. Do you need anything to be done by anyone? 
​[8/6, 8:55 PM] Mrigank Pawagi
    Not at the moment. I will delegate some additional tasks in the next dry lab meeting though. 
[8/7, 12:12 PM] Mrigank Pawagi(Preliminary) Work on Using LLMs to Improve the Biobricks Registry
    (Dry Lab, Human Practices) I have updated the following repository with documentation on the work that I was pursuing, for improving Biobricks registry entries using Large Language Models: https://github.com/iGEMIISc/biobricks
I would encourage everybody to go through the README, and if interested, also through the model_<name>.ipynb files and suggest any changes (you can make a PR or tell me here) in the documentation or elsewhere. If you want to explore LLMs yourself and would like to work on this, feel free to let me know. As I mentioned, this is work in progress! 
[8/7, 12:13 PM] Mrigank Pawagi
    We have put our foot in the door on this thing. We can take up again after a while and maybe for now focus on the other thing which we were planning (Biobricks visualizer)
[8/6, 7:10 PM] Mrigank PawagiFor PK
    (Dry Lab) GastroPlus is a proprietary software and we cannot even use it without asking for a quote. There is an open source (yay!) simulation software for PK modelling called PK-sim and it seems quite promising. I tried the UI and it looks pretty comprehensive. I will suggest that people who are working on PK modelling download it (from https://github.com/Open-Systems-Pharmacology/PK-Sim/releases/tag/v11.2.142) and maybe try it a little bit. Let us meet some time in the coming week and collate our previous findings to create something on PK-sim. In particular, I would want Tarushri, Sanjana and Anwesha to be involved since you have all been working on finding relevant data and models for a while. Please share what day & time works in the comments. 
[8/10, 8:27 PM] Sanjana D S
    Regarding the above, this video might help in familiarising with the modelling https://youtu.be/BPNk34DJ6AM
[8/10, 9:30 PM] Sanjana D S
    https://youtu.be/nqoAJ3rFnhw tutorial on pk sim
[8/13, 11:50 PM] Mrigank PawagiUpdates Meeting?
    Dry Lab 
I think we should meet sometime in the next week to get up to speed. Does Wednesday evening work for all of you? We will just discuss what we've been up to and how we will be moving forward with some of those things. Sheersh, we would be discussing some HP aspects as well.

Feel free to suggest alternate timings if the current suggestion does not work very well. 
[8/24, 12:05 AM] Mrigank PawagimRNA Optimization
    This is an updates post. As I mentioned on WhatsApp, I was able to install all necessary components for running RiboTree, and also fix some of the breaking errors in the tool (and also report them to the creators), to finally be able to run it. We ran it on 4 sequences today: Main sequence(seq), seq + 3' UTR, 5' + seq, and 5' + seq + 3'. Results (and input files) are in the git repository: https://github.com/iGEMIISc/mRNA-Optimization

The installation is done on one of the systems in the UG Computation Lab, and anybody interested in checking RiboTree out is welcome to do so. We will probably try exploring the configurations available in RiboTree to hopefully get even better results.

[8/6, 7:14 PM] Mrigank PawagiAptide & Fibronectin EDB Docking
    Sanika it seems the docking has been done, and all that we need to do is



	
Upload the output from GRAMM and PRODIGY to the Repo
	
Create a GIF (for aesthetic purposes 😅) of the dockings. This can be done easily using PyMol (which you must have installed during that Homology workshop). Let me know if you need any help (with this, or with the 1st point, or both)

Great job!
​[8/6, 7:18 PM] Mrigank Pawagi
    There's an additional task that you can pursue (other people are encouraged to help) after this: Can you check if, and how, we can submit our dockings to the PDB? There is a computed models category as well. 
(1 liked)Edited​[8/23, 7:52 AM] Mrigank Pawagi
    Sanika, can we also do some research on what the standard for K_d values is, for antibody-antigen interactions? 
(1 liked)​[8/23, 10:43 PM] Aditya Kamath Ammembal
    The standard Kd values are of the order of pico molar
​[8/23, 10:43 PM] Aditya Kamath Ammembal
    Aptamers are micromolar
​[8/23, 10:47 PM] Aditya Kamath Ammembal
    AFAIK, this needs to be confirmed thosweatgrinning
​[8/24, 12:01 AM] Mrigank Pawagi
    Aah, I see. We can try to find some source for this. 

​[8/24, 9:38 AM] Sanika Amol Borade
    
In general: "Most antibodies have KD values in the low micromolar (10-6) to nanomolar (10-7 to 10-9) range. High-affinity antibodies are generally considered to be in the low nanomolar range (10-9), with very high-affinity antibodies being in the picomolar (10-12) range."
​[8/24, 9:38 AM] Sanika Amol Borade
    



"ABX-IL8 binds to human IL-8 with high affinity (kd = 2 x 10^10 mol/L) and fails to cross-react with a panel of closely related chemokines."



(1 liked)Edited​[8/24, 9:38 AM] Sanika Amol Borade
    This is from the following paper: https://doi.org/10.1016%2FS0002-9440(10)64164-8
​[8/25, 1:20 AM] Mrigank Pawagi
    Great! Can this info be added to our README. Please make a Pull Request whenever possible. 
[8/26, 9:49 PM] Sheersh Sen
    Aditya Kamath Ammembal and Mrigank Pawagi, here are the papers I talked about. So firstly, I guess we'll try to look into the EPR effect in case of Endometriosis and how strong it is, followed by maybe highlighting important parts of the papers that have some actual quantitative data. As Prof Rachit mentioned, that seems to be the first part of actually coming up with a model for our system. Once we have some data on LNP accumulation and retention, we'll probably have to focus on the transfection efficiency aspect. Thereafter we use whatever mRNA translation data we have et cetera, but right now, this should have priority. 
(1 liked)[incancer.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/PKPDMathModels/incancer.pdf)[eprnanomeds.pdf] (https://indianinstituteofscience.sharepoint.com/sites/iGEM2023/Shared Documents/Dry Lab/PKPDMathModels/eprnanomeds.pdf)