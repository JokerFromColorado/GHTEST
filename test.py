wsdasdadsdas
wsdasdasd
asdadsdsf
sdfsdfsdf
dasd
asdasdasdsdasd
asdasdsad
asdasdadssd
adasdrsdstring fsdasdasdadsor test
saewr
wewerwrwer
wer
werwrw
r
we wer wrwe ew wer test 
rrwerwerwer
w
er
wer
wer
wer

wer
wer

w
er
wer
wer
wewer
ewrwer
we
wer
werweddasqweqwqwe


ddsfsdsd
fsdasdsdaasd
ads
d
as
sda
asd
as
d
sad
sadqweqweqwe
qwe
qwq
wwqe
qwe
asd

fewrwer345345345
534
3
45
345
345
345qewqweq
qwe
qeweqw

asdasdasertertertert
ert

DASasewrwewrewer

wertyrtyrytrytHi,

I am having problems with the GitHub integration - the commands are not working.

- My email address is the same on YouTrack and GitHub
- I have added the repository on GitHub and enabled the hook
- I have filled in root username and password on GitHub hook
- I am running YouTrack on self-installed Tomcat
- I pushed a commit with "Test #IBN-2 Fixed" (IBN-2 was in progress) and it wasn't updated to Fixed

YouTrack address: http://track.mblgrn.com
Github: http://github.com/georgios

What can I do to troubleshoot this? Log of the above commit operation above

Georgios


24 Apr 2013 15:25:17,090 INFO  [MainServlet                   ] [http request: /issue/IBN-2                        ] [internal@127.0.0.1] Start processing request /issue/IBN-2
24 Apr 2013 15:25:17,090 DEBUG [BaseApplication               ] [http request: /issue/IBN-2                        ] [internal@127.0.0.1] Created bean for session variables
24 Apr 2013 15:25:17,121 INFO  [MainServlet                   ] [http request: /issue/IBN-2                        ] [internal@127.0.0.1] Finish processing request /issue/IBN-2 in 31ms
24 Apr 2013 15:25:33,906 INFO  [MainServlet                   ] [http request: /projects                           ] [georgiosd@127.0.0.1] Start processing request /projects
24 Apr 2013 15:25:33,922 INFO  [MainServlet                   ] [http request: /projects                           ] [georgiosd@127.0.0.1] Finish processing request /projects in 16ms
24 Apr 2013 15:25:35,825 INFO  [MainServlet                   ] [http request: /editProject/IBN                    ] [georgiosd@127.0.0.1] Start processing request /editProject/IBN
24 Apr 2013 15:25:35,872 INFO  [MainServlet                   ] [http request: /editProject/IBN                    ] [georgiosd@127.0.0.1] Finish processing request /editProject/IBN in 47ms
24 Apr 2013 15:25:36,324 INFO  [MainServlet                   ] [ow_id=41 [l.E.tab_Fields:methodCall_showFieldList]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_Fields:methodCall_showFieldList]
24 Apr 2013 15:25:36,324 WARN  [Widget                        ] [ow_id=41 [l.E.tab_Fields:methodCall_showFieldList]] [georgiosd@127.0.0.1] Try to add null commandResponse.
24 Apr 2013 15:25:36,324 WARN  [Widget                        ] [ow_id=41 [l.E.tab_Fields:methodCall_showFieldList]] [georgiosd@127.0.0.1] Try to add null commandResponse.
24 Apr 2013 15:25:36,340 INFO  [MainServlet                   ] [ow_id=41 [l.E.tab_Fields:methodCall_showFieldList]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_Fields:methodCall_showFieldList] in 16ms
24 Apr 2013 15:25:39,257 INFO  [MainServlet                   ] [events?window_id=41 [l.E.tab_GitHub.rl.edit:click]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_GitHub.rl.edit:click]
24 Apr 2013 15:25:39,257 INFO  [MainServlet                   ] [events?window_id=41 [l.E.tab_GitHub.rl.edit:click]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_GitHub.rl.edit:click] in 0ms
24 Apr 2013 15:25:39,554 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:39,554 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:25:41,316 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:25:41,332 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 16ms
24 Apr 2013 15:25:42,330 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:42,330 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:25:44,858 INFO  [MainServlet                   ] [ts?window_id=41 [l.E.tab_GitHub.egrd.cancel:click]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_GitHub.egrd.cancel:click]
24 Apr 2013 15:25:44,858 INFO  [MainServlet                   ] [ts?window_id=41 [l.E.tab_GitHub.egrd.cancel:click]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_GitHub.egrd.cancel:click] in 0ms
24 Apr 2013 15:25:45,326 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:45,326 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:25:46,652 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:25:46,667 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 15ms
24 Apr 2013 15:25:48,336 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:48,336 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:25:51,425 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:51,441 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 16ms
24 Apr 2013 15:25:53,687 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:25:53,703 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 16ms
24 Apr 2013 15:25:54,436 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:54,436 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 16ms
24 Apr 2013 15:25:57,338 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:25:57,338 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:00,333 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:00,333 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:00,660 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:00,660 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 0ms
24 Apr 2013 15:26:03,328 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:03,328 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:06,339 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:06,339 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:07,649 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:07,665 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 16ms
24 Apr 2013 15:26:09,412 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:09,412 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:12,438 INFO  sdfsdsdf
sd
fsd
fsd[MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:12,438 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:14,654 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:14,669 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 15ms
24 Apr 2013 15:26:15,340 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:15,340 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:16,323 INFO  [MainServlet                   ] [http request: /_events?window_id=41 [_heart_beat] ] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [_heart_beat]
24 Apr 2013 15:26:16,323 INFO  [MainServlet                   ] [http request: /_events?window_id=41 [_heart_beat] ] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [_heart_beat] in 0ms
24 Apr 2013 15:26:18,335 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:18,335 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:21,330 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:21,330 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:21,658 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:21,658 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 0ms
24 Apr 2013 15:26:24,341 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:24,341 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:27,352 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:27,352 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:28,662 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:28,662 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 0ms
24 Apr 2013 15:26:30,378 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:30,378 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:33,342 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:33,342 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:35,667 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:35,682 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 15ms
24 Apr 2013 15:26:36,384 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:36,384 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:39,333 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:39,333 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:42,344 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:42,344 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:42,671 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:42,687 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 16ms
24 Apr 2013 15:26:45,339 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:45,339 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:48,428 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:48,428 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 0ms
24 Apr 2013 15:26:49,676 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick]
24 Apr 2013 15:26:49,691 INFO  [MainServlet                   ] [ts?window_id=41 [l.AdminMenu.adminMenuTicker:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.AdminMenu.adminMenuTicker:tick] in 15ms
24 Apr 2013 15:26:51,345 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Start processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick]
24 Apr 2013 15:26:51,360 INFO  [MainServlet                   ] [TeamcityBuildTypeMappingList.refreshStatuses:tick]] [georgiosd@127.0.0.1] Finish processing request /_events?window_id=41 [l.E.tab_TeamCity.TeamcityBuildTypeMappingList.refreshStatuses:tick] in 15ms

