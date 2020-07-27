# Instructor notes for PHP Scripting
The 2015 version of CyberAces included a module on PHP web server scripting, but that is no longer included in the current CyberAces.  When I taught the old CyberAces version, I found that PHP was a good place to demonstrate basic web attacks.  Therefore, I still teach the PHP modules that have to do with installation, basic HTML, and how to use the troubleshooting modes of PHP.  I skip the modules on PHP coding (operators and flow control) and do modules I have written for basic web attacks.

## Labs I currently use
- PHP Lab 1 Web Server Installation
- PHP Lab 2 HTML Basics
- PHP Lab 3 Troubleshooting PHP Scripts
- PHP Lab 6 Local File Inclusion
- PHP Lab 7 Cross Site Scripting
- SQL Injection Lab
- Holiday Hack Trail--Basic Web Attacks

## SQL Injection Lab
The SQL Injection lab was developed by Justin Keane (@madirish2600, http://www.madirish.net/).  I have modified Justin's CTF 7 lab (https://sourceforge.net/projects/lampsecurity/) to fit into a 2.5 hour class period.  To do the lab, you need a Kali Linux VM and you need to download Justin's image at https://sourceforge.net/projects/lampsecurity/files/CaptureTheFlag/CTF7/CTF7plusDocs.zip/download.  It is a fun lab which uses sqlmap to breach an insecure web server with SQL injection and eventually gain root on the machine (root dance, anyone?)

## Holiday Hack Trail--Basic Web Attacks
This is a fun lab using the Holiday Hack Trail Challenge written by Chris Elgee (@chriselgee) for the 2019 Holiday Hack Challenge (https://holidayhackchallenge.com/2019/).  It uses Chrome's built-in developer tools to doctor responses to a game site, Holiday Hack Trail (sounds like Oregon Trail), to win the game.  The Holiday Hack Trail web site ( https://trail.elfu.org/gameselect/?playerid=JebediahSpringfeld) is maintained by CounterHack.org, so no resources are required.  The last, hard, challenge involves cracking the site's scheme for encrypting cookies.  My students enjoyed it last year.
