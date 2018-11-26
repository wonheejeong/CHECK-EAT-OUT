# CHECK-EAT-OUT 




<p align="center">
<br><br>
<img width =200 src = "https://user-images.githubusercontent.com/28107452/49039284-b37d7480-f202-11e8-81b6-f041ebd3351a.png">
</p>
<br><br>


Description
---------------

As security threats increase, the importance of "secure-coding" has grown. <br>
Companies and developers have found vulnerabilities in code development through code review and simulation. <br>
However, it takes a lot of time, so many companies are now benefiting from the use of automated tools. <br>
The problem with our team is that the "test case" used in simulation and automation tools is being updated manually.<br>
With the advent of automation tools, the "test case," which is the basis for diagnosing, has caused a gap between the occurrence of security incidents and the reflection on the source code. <br>
To address this, Secugo will creates a "test case."
<br>
>보안 위협이 증대됨에 따라, "시큐어 코딩"의 중요성이 중대가 되었습니다. <br>
이에 기업 및 개발자들은 코드 리뷰 및 모의해킹을 통해 개발 된 소스코드의 취약점을 찾아왔습니다.<br>
다만, 이는 많은 시간이 소요되기에 현재는 많은 기업들에서 자동화 된 도구를 도입하여 도움을 받고 있습니다. <br>
 저희 팀이 바라보는 문제는, 모의해킹 및 자동화 툴에서 사용되어지는 “테스트 케이스”가 수작업으로 갱신되고 있다는 것입니다. <br>
 자동화 툴의 등장으로 진단 속도는 월등히 상승하였으나, 이에 진단 기준이 되는 “테스트 케이스” 는 늦은 업데이트로 인해 보안 사건의 발생과 소스코드상의 반영 사이에 공백이 생기게 됩니다. <br>
 SecuGo는 이를 해소하기 위하여 “테스트 케이스” 생성 컨텐츠를 만들어 보고자 합니다.
<br><br>

Development Background
-----------------------
- Mass data generation, as it is called IT consumption. Many of these cyber attacks are also on the rise.
- According to the IBM X-Force Tech report, 41% of new vulnerabilities occur in web applications. In addition, vulnerabilities such as known XSS and SQL injection continue to grow.
>-  IT의 소비화 라고 불려 질만큼, 대량의 데이터가 발생. 그로인한 많은 사이버 공격 또한 증가하는 추세입니다.
>-  IBM X-Force 테크 보고서에 따르면, 신규 취약요소 중 41%는 웹 어플리케이션에서 발생한다고 합니다. 또한, 이미 알려진 XSS 및 SQL Injection과 같은 취약점도 계속해서 증가하는 추세입니다.
<br><br>
Characteristics
---------------
- Some sort of Secure coding tool designed to help developers develop.
- Provide comments on areas where threats may exist for the developer's code.
- Provides a coding guide for real-time, secure coding from threats.
>- 개발자들의 개발을 수월하게 돕고자 만들어진 일종의 Secure coding tool.
>- 개발자의 코드에 대해 위협이 존재할 수 있는 부분들에 대한 코멘트를 제공합니다.
>- 코딩 가이드를 제공해줌으로서 위협으로부터 실시간으로 안전한 코딩을 구현할 수 있습니다.
<br><br>
Development Contents
----------------------

- Collect incident cases from security case sites such as CWE,ANS,OWASP
- Perform a custom NLU, transform the data into categorised security data.
- Subsequently, pattern matching is used to compare all source codes and the above cases shown in Github.
- When developers write the above code, they create a website and IDE plug-in that tells them the possibility of vulnerabilities.(The creation of IDE plug-ins is set as additional attainment targets during the project)

>-  CWE,SANS,OWASP 와 같은 보안사건 사례 사이트에서 사건 케이스를 수집(Crawling)<br>
>-  위 데이터를, 커스텀 된 NLU를 수행, 카테고리화 된 보안 데이터로 변형합니다.<br>
>-  이후, 패턴 매칭 작업을 통해 Github에 공개된 모든 소스코드와 위의 케이스를 비교 분석합니다.<br>
>-  위와 유사 코드를 개발자가 작성시, 취약점 가능성을 알려주는 웹 사이트 및 IDE플러그인을 제작합니다.(IDE 플러그인 제작은 프로젝트 기간 상, 추가 달성 목표로 설정)<br>
<br><br>

Key Application Technologies
-----------------------------

-Customized NLU: 기존 자연어 분석의 NLU를 security 분야로 customize합니다.
-Pattern Matching: 수집(Crawling)된 테스트 케이스와 개발자의 코드를 비교 시 사용합니다.
-Crawling: 보안사건 케이스들을 수집합니다.

<br><br>
Development Environment
------------------------
-Windows10 / Ubuntu-Bionic Beaver
-Pycharm, Visual Studio 14.0, Eclipse etc
-Python, JSP, Node.js etc
-MySQL 5.7

<br><br>
Demonstration video
--------------




<br><br>

Development environment
------------------------
+ Python 3.6.5
+ Flask
+ MySQL

<br><br>

Used API
----------------
+ IBM Watson NLU API

<br><br>

License
--------------
© All rights reserved. Design: wonhee Jeong.
* 본 프로젝트는 한이음 멘토링 프로젝트로 진행되었습니다.
