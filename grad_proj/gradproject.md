---
layout: page
title: Graduate Project
nav_order: 6
nav_exclude: false
description: Specifications for the grad project for Data 200.
markdown: kramdown
---
# Graduate Project
{:.no_toc}

* TOC
{:toc}

## Introduction

The graduate project is offered only to students enrolled in Data C200 or CS C200A. Other students are welcome to explore the questions and datasets in the project for personal learning, but their work will not be graded or counted towards their final grades.

The purpose of the project is to give students experience in both open-ended data science analysis and research in general. In this project, you will work with **one or any combination** of the following datasets provided to you to explore research questions that you define.

**Project criteria**: In addition to the general guidelines, each dataset option below has its own set of additional requirements for Report Format and Submission. Be sure to consult the correct section for your project option.

**Grading**: You will receive peer review feedback before the final deadline, and you are expected to incorporate the peer feedback into the final report and presentation. You will be graded on both the final report and presentation, as well as [deliverables](#deliverables) before the submission of the final reports, including your peer reviews.

**Teamwork**: You can work alone or in a group with **at most two other students**. If you are interested in working with others, we have an [Ed post](https://edstem.org/us/courses/25695/discussion/1789891) for teammate search. Everyone in the same group will receive the same grade. The group size will be taken into consideration when grading.

## Timeline


| Date (by EOD at 11:59pm Pacific) 	| Event / Deliverable           | Link           |
|--------------------------	|---------------------------------------------	|---------------------------------------------	|
| 9/30                       | Research proposal and project groups due    	| [Preliminary Form](https://docs.google.com/forms/d/e/1FAIpQLSc3uhrp0pj0iw9Iaw4gGrok9LeZXe1alVXJcfzfqbr0-ZiokA/viewform?usp=sf_link) |
| 10/14                      | Project checkpoint 1 Due                      | |
| 11/18                      | Project checkpoint 2 Due                      | |
| 12/2                    	| First draft of final report due             	| |
| 12/3                   	  | Peer review open                            	| |
| 12/7                       | Peer review due                             	| |
| 12/14                       | Revised final report due                    	| |
| 12/14                      | Presentation video due                      	| |
| 12/16                      | Presentation video released (at discretion) 	| |

**Late Policy:** You may submit the **final report** and the **presentation video** late with a 10% penalty to that portion of your project for each day it is late. You may submit up to two days late. Submission times are rounded up to the next day. That is, 2 minutes late = 1 day late.

## Deliverables and Grade Breakdown

| Deliverable                          	| Weight 	|
|--------------------------------------	|--------	|
| Research proposal and project groups 	| 10%    	|
| Checkpoints                           |  0%     |
| Submission of first draft            	| 10%    	|
| Peer review                         	| 15%    	|
| Final report: Analysis notebook      	| 20%    	|
| Final report: Project writeup        	| 30%    	|
| Final presentation video             	| 15%    	|

The project checkpoint is a quick Google Form to assess if you are making progress towards your goals.

## Datasets

This section contains the datasets we will provide to you to explore your research questions.

- You must incorporate **at least one** of the provided datasets.
- You are welcome to **bring in additional datasets** to complement the datasets provided here, but you must cite the sources and clearly describe the content of any additional data you use in the final report.

Should you need to connect together multiple datasets, please be sure to consult the [extra resource on causal inference](#extra-resources-causal-inference).

### Accessing Datasets

All the datasets provided by us can be found inside the following link on Google Drive:

<p align="center">
<a href="https://drive.google.com/drive/u/0/folders/1WGxxvFMqXutk3WKGqbHYJx0urmQp9Lbw">Graduate Project Datasets Google Drive</a>
</p>

If you wish to work on Datahub, use the following instructions on how to easily move the data from Google Drive onto Datahub (keep in mind that your Datahub kernel can only manage 2GB of memory at maximum).

If you wish to work on the project locally, you can also download the zip files containing the datasets for each topic.

#### **How to Pull Data from Google Drive directly onto Datahub**
{:.no_toc}

1. _Get the Google Drive ID of the file_. You can do this by first getting the URL of the file. You do this by right-clicking on the file in Google Drive and pressing 'Get Link'. Once you have the URL, you can find the ID by looking for the set of characters after the /d/ in the url. For example, in the following url: `https://drive.google.com/file/d/16-4O_lJGioPC5G9il4vR_XrCgJ3J9_zK/view?usp=sharing` , the Google Drive ID would be `16-4O_lJGioPC5G9il4vR_XrCgJ3J9_zK`.
2. _Download the data_. Once you have the Google Drive ID of the file, you can use the `utils.py` file inside the `grad_proj` directory on your Datahub. This file has a number of useful functions for downloading data. You'll want to use `fetch_and_cache_gdrive`. You will call the function in a notebook. The function takes in two arguments: **(1) Google Drive ID** that you got in the previous step, and **(2) name of the file**. Calling the function will generate a `data` folder and place the file into that folder, using the name you came up with as the second argument of the function.

Hopefully the above steps help you to access the data on Google Drive. There are other ways to move the data onto Datahub. Consider looking into [`gdown`](https://github.com/wkentaro/gdown) or just downloading the data from Google Drive and uploading it to Datahub manually.

Take a look at the other functions in `utils.py` if you'd like to use other data sources to supplement your project. 


### Topic 1: COVID-19

#### Dataset A: Testing and Mortality Statistics
{:.no_toc}

This dataset contains US reports on COVID-19 testing and cases from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) and CDC (Centers for Disease Control and Prevention). You can access all the data within the `Topic 1/Dataset A` directory on Google Drive:

* `csse_covid_19_daily_reports_us.csv` contains US daily reports ([documentation](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data#usa-daily-state-reports-csse_covid_19_daily_reports_us))
* `cdc_death_counts_by_sex_age_state.csv` contains US weekly reports on deaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age, group, and state. ([documentation](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku))
* `cdc_death_counts_by_conditons.csv` contains US weekly reports on health conditions and contributing causes mentioned in conjunction with deaths involving COVID-19. ([documentation](https://data.cdc.gov/NCHS/Conditions-contributing-to-deaths-involving-corona/hk9y-quqm))

You must choose to work with **at least 2 of the reports** above in your analysis.

#### Dataset B: Impact on Health Care
{:.no_toc}

This dataset contains reports from the Household Pulse Survey launched by NCHS in partnership with the U.S. Census Bureau; it focuses on how COVID-19 has affected survey correspondents' mental health and their access to health care. In addition, it provides statistics on usage of telemedicine by healthcare providers. You can access all the data within the `Topic 1/Dataset B` directory on Google Drive:

* `nchs_covid_indicators_of_anxiety_depression.csv` contains survey estimates of responses to questions that are indicators of anxiety or depression based on reported frequency of symptoms within the past week. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Anxiety-or-Depression-Based-on-Repor/8pt5-q6wp))
* `nchs_covid_mental_health_care.csv` contains survey estimates of responses to questions that ask if participants have accessed mental health care in the past 4 weeks. ([documentation](https://data.cdc.gov/NCHS/Mental-Health-Care-in-the-Last-4-Weeks/yni7-er2q))
* `nchs_covid_health_insurance_coverage.csv` contains survey estimates of responses to questions that ask about participants' health insurance coverage. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Health-Insurance-Coverage-at-the-Tim/jb9g-gnvr))
* `nchs_covid_reduced_access_to_health_care.csv` contains survey estimates of responses to questions that ask if participants have experienced delay or been refused health care due to COVID-19. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Reduced-Access-to-Care-Due-to-the-Co/xb3p-q62w))
* `nchs_covid_telemedicine_usage.csv` contains survey estimates of responses to questions that ask if healthcare providers offered telemedicine (including video and telephone appointments) -- both during and before the pandemic -- and about the use of telemedicine during the pandemic. ([documentation](https://data.cdc.gov/NCHS/Use-of-Telemedicine-During-COVID-19/8xy9-ubqz))

You must choose to work with **at least 3 of the reports** above in your analysis.

#### Dataset C: Ongoing Researches
{:.no_toc}

This dataset contains (in full-text and metadata form) scholarly articles related to COVID-19. The data are optimized for machine readability and made available for use by the global research community. The dataset is intended to mobilize researchers to generate new insights from the articles in support of the fight against this infectious disease. You can access all the data within the `Topic 1/Dataset C` directory on Google Drive:

* `covid_open_research_dataset.txt` contains the link that will guide you to obtain the full-text and metadata dataset of COVID-related research articles. ([documentation](https://azure.microsoft.com/en-us/services/open-datasets/catalog/covid-19-open-research/))

### Topic 2: Climate and the Environment

#### Dataset A: General Measurements and Statistics <a name="2-a"></a>
{:.no_toc}

This dataset contains some general statistics and measurements of various aspects of the climate and the environment. You can access all the data within the `Topic 2/Dataset A` directory on Google Drive. It includes the following reports:

- `daily_global_weather_2020.csv` contains data on daily temperature and precipitation measurements. To learn how to use the data from this file, please read the following section on the first report.
- `us_greenhouse_gas_emissions_direct_emitter_facilities.csv` and `us_greenhouse_gas_emission_direct_emitter_gas_type.csv` contain data reported by EPA (Environment Protection Agency) on greenhouse gas emissions, detailing the specific types of gas reported by facilities and general information about the facilities themselves. The dataset is made available through EPA's [GHGRP (Greenhouse Gas Reporting Program)](https://www.epa.gov/ghgreporting).
- `us_air_quality_measures.csv` contains data from the EPA's AQS (Air Quality System) that measures air quality on a county level from approximately 4000 monitoring stations around the country. ([source](https://data.cdc.gov/Environmental-Health-Toxicology/Air-Quality-Measures-on-the-National-Environmental/cjae-szjv))
- `aqi_data` contains more data from the EPA from a number of sites across a multitude of different metrics. ([source](https://aqs.epa.gov/aqsweb/airdata/download_files.html))

The following subsection contains more details on how to work with the first report on global daily temperature and precipitation:

The first report on daily temperature and precipitation is measured by weather stations in the [Global Historical Climatology Network](https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn) for January to December 2020.

The data in `daily_global_weather_2020.csv` is derived from the source file at https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2020.csv.gz.

To help you get started with a dataset of manageable size, we have preprocessed the GHCN dataset to include only the average temperature and precipitation measurements from stations that have both measurements. Each row in the preprocessed dataset contains both the average temperature and precipitation measurements for a given station on a given date.

If you wish to explore the climate data for a different year, you can use the `GHCN_data_preprocessing.ipynb` notebook to download and perform the preprocessing described above. Please be advised that depending on the dataset size for a given year, `GHCN_data_preprocessing.ipynb` may not run on DataHub. We will not be providing infrastructural support for running the notebook, but you are welcome to run it on a different machine you have access to or ask a GSI to dump the data for you.

The data contains only the (latitude, longitude) coordinates for the weather stations. To map the coordinates to geographical locations, the [reverse-geocoder](https://github.com/thampiman/reverse-geocoder) package mentioned in the [References](#coordinates) section might be helpful.

#### Dataset B: Biodiversity in the Ecosystem
{:.no_toc}

This dataset contains studies focused specifically on the impact of environmental and climate changes on biodiversity and the local ecosystems. You can access all the data within the `Topic 2/Dataset B` directory on Google Drive. It includes the following reports:

- `bioCON_plant_diversity.csv` contains data collected as part of an ecological experiment, BioCON (Biodiversity, CO2, and Nitrogen), that started in 1997 and focused on studying biodiversity within the plant species at Cedar Creek Ecosystem Science Preserve. ([documentation](https://search.dataone.org/view/https%3A%2F%2Fpasta.lternet.edu%2Fpackage%2Fmetadata%2Feml%2Fknb-lter-cdr%2F339%2F9))
- `plant_pollinator_diversity_set1.csv` and `plant_pollinator_diversity_set2.csv` contain ecological data collected from a long-term observation study from 2011 to 2018 that focuses on plant-pollinator interaction and its impact on local biodiversity. ([documentation](https://search.dataone.org/view/https%3A%2F%2Fpasta.lternet.edu%2Fpackage%2Fmetadata%2Feml%2Fknb-lter-and%2F5216%2F6))
- `national_parks_biodiversity_parks.csv` and `national_parks_biodiversity_species.csv` contain data published by the National Park Service on animal and plant species identified in individual national parks.

### Topic 3: Emerging Researches and Technologies <a name="tech"></a>

#### Dataset A: Space Exploration
{:.no_toc}

This dataset contains a set of reports from pioneering researches that explore the outer space. Much of the data from these studies have provided a rich foundation for a variety of large-scale research projects that explore widely discussed topics such as habitable exoplanets or search for extraterrestrial life.

You can access all the data within the `Topic 3/Dataset A` directory on Google Drive. It includes the following reports:

- `kepler_exoplanet_search.csv` contains data collected by NASA from the Kepler Space Observatory as part of a long-term study on finding habitable exoplanets from over 10,000 candidates. ([source](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi))
- `kelper_planetary_system_composite.csv` contains data collected by NASA from the Kelper Space Observatory as part of an ongoing study that tabulates all confirmed planetary systems outside the solar system. You are encouraged to use the composite data in conjunction with the exoplanet search results above. ([source](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars))
- `nasa_neows.csv` contains data collected from NASA's [NeoWs (Near Earth Object Web Service)](https://neowise.ipac.caltech.edu/) that collects information on near earth asteroids.

#### Dataset B: Recommender Systems
{:.no_toc}

A recommender system is an information filtering system that focuses on predicting the preference a user would give to an item by predicting its rank; it is used in a variety of areas, such as search engines, online shopping platforms, etc. This dataset contains a set of reports on various tools using a recommender system.

You can access all the data within the `Topic 3/Dataset B` directory on Google Drive. It includes the following reports:
- `fitness_recommendation.txt` contains a link to access the fitness data from sequential sensors for various workouts. ([documentation](https://sites.google.com/eng.ucsd.edu/fitrec-project/home))
- `amazon_reviews.txt` contains a link to access the data on a subset of Amazon product reviews. The report includes metadata such as ratings and text on the reviews and general information about the product. ([documentation](https://nijianmo.github.io/amazon/index.html))

## Extra Resources: Causal Inference

When studying the relationship between datasets, you might want to consult the following references on causality vs. correlation. Oftentimes, it is tempting to make claims about causal relationships when there is not enough evidence from the data to support such claims. Please review the following references, or other reputable references that you find on the topic to familiarize yourself with relevant concepts and methods.

* [Data 102  Data, Inference, and Decisions Spring 2020: Lecture 13: Causal Inference I. Moritz Hardt.](https://data102.org/sp20/assets/notes/notes13.pdf)
* [Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC.](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* [Advanced Data Analysis from an Elementary Point of View by Cosma Rohilla Shalizi](https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/)
