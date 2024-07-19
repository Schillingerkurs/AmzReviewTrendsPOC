---
marp: true
author: Felix Schilling
theme: academic
title: Slideshow Felix Schilling
paginate: true

style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---
<style>
  img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
  }

  @import 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css';
</style>

<!-- _class: title -->



# Generative AI 

<br/>
<!-- _class: subtitle -->

## Case Interview for ADC

<div class="columns">
<div>

July 22<sup>nd</sup>  2024

Felix Schilling, PhD

</div>
<div>

<img src="../data/raw/profile_Felix_Schilling.jpg" alt="profil_felix" style="max-width: 55%; border-radius: 50%;">

</div>
</div>


---
This presentation 

- Amazon Review Trends  POC (20 min)
  - Project plan
  - POC model

-  Retrievel-Augmented Generation (RAG) (10 min)


---

#  Project plan

- Initial Stakeholder Consultation
- POC pipeline 
  - batch process , API , cleaning
  - Feature generation
  - Model Development 
  - Deployment
- Visualization and Reporting
- Stakeholder Feedback and Next steps 


---
# The challenge

 Sequential text data: 
  - 1) Text dimension (structured and unstructured)
  - 2) Time dimension

= Complex data space, i.e. plenty of options to improve products and services. **We need to focus on the core needs of the stakeholders.**

---
# 1. Initial Stakeholder Consultation

We need to understand role, needs and metrics for the stakeholders improve their  products and services.


- Example:
  - Role: Product owner 
  - Task: Needs to know at what point in time they receive valuable feedback.
  - Metric: Estimate feedback can one expect.

- Example 2: 
  - Role: Compliance Specialist for the SEC.
  - Needs: Needs to know of miss use of products, to avoid lawsuits 
  - Metric: Product that reviews that mention drug abuse. 


---

# Data Pipeline

 - Figure: Batch process, API
 - feature Engeninnering
 - Model 
 - Deployment

 
- Named entity recognition (NER)
- relationship extraction 
- **Implementation:** Spacy 


---
#  Pipeline (Batch Processing, API Call & NLP)

<img src="flowdiagramm\1721376795149.png" alt="flow_diagramm" style="max-width: 61%;">


---

# Example Dashboard: Product owner.

- Streamlit

- Dashboards for the specific user case.

Guarantee that the Alg is 
- closely monitored
- future proof
- compliant with all relevant regulations.
- Uphold ethical standards in the development and deployment of AI.

---

# 3. Model Development

RAG (Retrieval-Augmented Generation) Integration
- For information retrieval to enhance accuracy.
- We "feed" domain specific knowledge into a pretrained model.

**Implementation:**  Ollama
- Keep and eye on existing workflows and systems.

---

# 4. Training & Validation

- Review Data Preprocessing
- Training and fine-tune using domain-specific data.
- Validation
  - Cross-validate using separate datasets.
  - Error analysis and refine the model.


Goal: A robust model !
 - make sure we meet the predefined accuracy efficiency metrics.

If the model is not good enough: 
- Circle back to domain specific experts: What mistakes does the model do wrong?
- Select better relevant/data 
- Simplify classification.

---

# 5. Deployment & Monitoring

Deployment (in test environment):
- Integrate into existing infrastructure.
- **Implementation:**  Docker
- Ensure compatibility with data pipelines and user interfaces.
- Show deployed model to stakeholders w. domain knowledge first.


Monitoring:
- Set up real-time monitoring for performance tracking.
- Implement feedback loops for continuous improvement.
- **Implementation:**  Streamlit, PowerBi, etc.


---


# RAG


---

# Disclaimer

I created these slides using the following VS extensions 
- Copilot 
- Marp for VS Code


---

# Thanks!

- [felix.s.schilling@gmail.com](mailto:felix.s.schilling@gmail.com)
- [schillingerkurs.github.io](https://schillingerkurs.github.io/)

</div>



