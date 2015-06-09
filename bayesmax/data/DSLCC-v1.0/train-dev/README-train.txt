VarDial - DSL Shared Task (DSL Corpus Collection)

Website: http://corporavm.uni-koeln.de/vardial/sharedtask.html
Contact: Liling Tan <dsl.sharedtask@gmail.com>

Training and Development data : 21 Mar 2014

The DSLCC comprises news data from various corpora to emulate the diverse news 
content across different languages.

== Format Description ==

The training and development data contains 3 files (including this README).
i. 		devel.txt
ii. 	train.txt
iii.	README

The devel.txt contains 18,000 sentences for each language. 
The train.txt contains 2,000 sentences for each language.
All sentences are encoding in latin script UTF-8.

Each line in the .txt files are tab-delimited in the format:
sentence<tab>group<tab>language

== Evaluation ==

The test data realeased on 21 Apr 2014, will only contain sentences without
its language/variety group information.

IMPORTANT, please note the following to facilitate the evaluation:

(i) provide the system output as how the training and development data was 
formatted, without changing the order of the test sentences:
sentence<tab>group<tab>language

(ii) Please name your submission files with the following convention,
all in lowercase:
team_name-system_name-open_or_close-run#.txt

For example, if your team_name is "USAAR" , system_name is "DisLang" and it's an
open submission and it's the 1st run that you want to submit, the submission
file should be as such:
usaar-dislang-open-run1.txt

(iii) Please also compress ALL run submissions into a single file and send it to
dsl.sharedtask@gmail.com before the submission deadline (23 Apr), please name
compressed file in the following format: (team_name-system-name.zip)
For example:
usaar-dislang.zip

(iv) Do specify in the email title when sending the compression submission file,
e.g. (team_name DSL2014 submission)
Title: USAAR DSL2014 submission

(iv) Each team is ONLY allowed to submit 3 runs for closed and/or 3 runs for 
open task, (6 runs in total for teams participating in both)

(iv) Along with the systems runs, submit a short description of your system.
This is to facilitate the description of the systems in the summary/finding 
paper for the shared task. 


== DSL schedule ==

Training set release: March 20th, 2014
Test set release: April 21st, 2014
System submissions due: April 23rd, 2014 (23:59 EST)
Results announced: April 30th, 2014
Short papers deadline: May 30th, 2014
Feedback: June 20th, 2014
Camera-ready versions: June 27th, 2014

== Organizers ==

Marcos Zampieri, Saarland University, Germany
Liling Tan, Saarland University, Germany
Nikola Ljubešić, University of Zagreb, Croatian
Jörg Tiedemann, Uppsala University, Sweden
