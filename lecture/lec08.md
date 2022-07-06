---
layout: page
title: Lecture 8 –  Intro to Modeling, Simple Linear Regression
nav_exclude: true
---

# Lecture 8 -  Intro to Modeling, Simple Linear Regression

Presented by Anirudhan Badrinath and Dominic Liu

Content by Fernando Pérez, Alvin Wan, Suraj Rampure, Allen Shen, Joseph Gonzalez, Andrew Bray, Josh Hug, Lisa Yan, Ani Adhikari, and Sam Lau

- [slides](https://docs.google.com/presentation/d/1O0ywsG7f_iQitSh_GVyhqDXhAYA8HUELubz6iL1c_Oo/edit?usp=sharing){:target="_blank"}
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FDS-100%2Fsu22&branch=main&urlpath=lab%2Ftree%2Fsu22%2Flec%2Flec08%2Flec08.ipynb){:target="_blank"}
- [recording](https://bcourses.berkeley.edu/courses/1515881/external_tools/78985){:target="_blank"}
- supplemental recording: [SLR Derivation](https://youtu.be/HSgdHzq2uqo){:target="_blank"}


<!-- **The Quick Checks for this lecture are not yet ready to be released; please check back later.** A reminder – the right column of the table below contains _Quick Checks_. These are **not** required but suggested to help you check your understanding.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Video</th>
<th>Quick Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>8.1</strong> <br>Introduction</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/XR9NzKF-I_U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td></td>
</tr>
<tr>
<td><strong>8.2</strong> <br>Motivation</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/EQSvbsTuuUs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/LUG5kwmSNFGdJkUF6" target="\_blank">8.2</a></td>
</tr>
<tr>
<td><strong>8.3</strong> <br>Terminology</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/5H17R49cdxQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="" target="\_blank">8.3</a></td>
</tr>
<tr>
<td><strong>8.4</strong> <br>Creating Tables</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/QAABu0CoO38" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="" target="\_blank">8.4</a></td>
</tr>
<tr>
<td><strong>8.5</strong> <br>Querying Rows</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/Aw69PRyFUto" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://forms.gle/nMEo7ZdvxHNf3JAx5" target="\_blank">8.5</a></td>
</tr>
<tr>
<td><strong>8.6</strong> <br>Querying Groups</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/WsyA75ppEAU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="" target="\_blank">8.6</a></td>
</tr>
<tr>
<td><strong>8.7</strong> <br>Practice</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/LKyJWkGo8d0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="" target="\_blank">8.7</a></td>
</tr>
<tr>
<td><strong>8.8</strong> <br>Conclusion</td>
<td><iframe width="300" height="300" height src="https://www.youtube.com/embed/CE8QcsBkwFs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="" target="\_blank">8.8</a></td>
</tr>
-->
