# Student-Management-System


deployed-link: "https://studentmarksdatabase.herokuapp.com/" 

Note: this is a web application designed for desktop . 

functionalities:

1.It has four html pages(homepage.html,enter_marks.html,update_marks.html,leaderboard.html) and one python file which contains code of complete backend( connection for database,searching method,sorting methods,updating method).

2.Homepage contains two buttons ('enter_marks' and 'leaderboard').

3.In 'Enter_marks.html' page contains a form for filling the details of  student details and marks. It also contains three buttons ('home','leaderboard','update marks')
-->'home' button redirects to homepage.
-->'leaderboard' button redirects to leaderboard page.
-->'update marks' button redirects to update_page to update the details when we enter worng details.

4.In 'Update_marks.html' page contains a form for filling the details of student roll number and marks when the student entered wrong marks.

5. 'Update_marks.html' page gives alert message when wrong roll numbers is entered.It wont update the details.

6. 'Enter_marks.html' page wont accept for submitting same roll number for twice. It gives alert message showing "roll number already sumitted his or her details".

7. In 'Leaderboard.html' pagehas a Grid to display the rankings of the students based on percentage by default

8. 'Leaderboard.html' page contains 5 buttons('home','enter_marks','sort by name','sort by roll number','sort by rank').
-->'home' button redirects to homepage.
-->'leaderboard' button redirects to leaderboard page.
-->'sort by name' button is used for sorting student details according to  alphabeticals order.
-->'sort by roll number' button is used for sorting student details according to roll numbers.
-->'sort by rank' button is used for sorting student details according to their average.

9.'Leaderboard.html' page also contains searching bar for finding their details.if the student didn't submitted his details then it shows 'roll number has not submitted his marks'.

10.For connecting backend flask is used. MySQL Datastore for storing marks.

11."Bankend is designed in MVC architecture".

 

