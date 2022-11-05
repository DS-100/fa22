---
layout: page
title: Home / Schedule
nav_order: 1
description: A week-to-week description of the content covered in the course.
course:
  edstem: https://edstem.org/us/courses/25695/
  faq: https://ds100.org/fa22faq
currWeekNumber: 12
---

# Principles and Techniques of Data Science

{: .mb-2 }
UC Berkeley, Fall 2022
{: .mb-0 .fs-6 .text-grey-dk-000 }

<p>
<a href="https://berkeley.zoom.us/j/93160108652?pwd=dHlJcDlBSml4RGZ5NGhBTzFaS1dTZz09" class="btn btn-blue">Lecture Zoom</a>
<a href="https://edstem.org/us/courses/25695/discussion/1699429" class="btn btn-purple">Discussion Sign-Up</a>
<a href="https://oh.ds100.org/" class="btn btn-green">Office Hour Queue</a>
</p>
<!-- 
<p>
<a href="https://berkeley.zoom.us/j/94237360710" class="btn btn-blue">Lecture Zoom</a>
<a href="https://edstem.org/us/courses/15436/discussion/1021263" class="btn btn-purple">Discussion Sign-Up/Zoom</a>
<a href="{{site.baseurl}}/calendar" class="btn btn-green">Office Hour</a>
</p>
-->

<div>
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  <div class="role">
    {% for staffer in instructors %}
    {{ staffer }}
    {% endfor %}
  </div>
</div>

Jump to current week: [here](#week-{{page.currWeekNumber}}).

+ Frequently Asked Questions: Before posting on the [class Ed]({{page.course.edstem}}), please read the [class FAQ page]({{page.course.faq}}).
+ The [Syllabus]({{site.baseurl}}/syllabus) contains a detailed explanation of how each course component will work this Fall, please take time to take a look.
+ **Note:** The schedule of lectures and assignments is subject to change.

<!--
+ The [Syllabus]({{site.baseurl}}/syllabus) contains a detailed explanation of how each course component will work this summer, given that the course is being taught entirely online.
+ Textbook readings are optional and actively in development. See the [Resources]({{site.baseurl}}/resources/#textbook) for more details.
+ **Note:** The schedule of lectures and assignments is subject to change.
-->

<!--
Jump to current week: [here](#week-{{page.currWeekNumber}}).

+ Lecture is hybrid: in-person in Li Ka Shing 245 and online via Zoom (see link above). Recordings will be posted within 12 hours of live lecture.
+ **Frequently Asked Questions:** Before posting on the [class Ed]({{page.course.edstem}}), please read the [class FAQ page]({{page.course.faq}}).
+ Join Ed: [here]({{page.course.edstem_join}}).
+ Textbook readings are optional and actively in development. See the [Resources]({{site.baseurl}}/resources/#textbook) for more details.
+ **Note:** The schedule of lectures and assignments is subject to change.

<br><br>
-->


<a name="schedule"></a>
## Schedule

{% for module in site.modules %}
<a name="week-{{module.weekNumber}}"></a>
{{ module }}
{% endfor %}
