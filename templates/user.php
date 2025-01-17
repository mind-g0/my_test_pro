<!DOCTYPE html>
<html>
<head>
    <title>User</title>
    <style>
        p{
            color: red;
            font-size: 50px;
        }
    </style>
</head>
<h1> hello {{name}} </h1>
<p> the replas shuld be in tow {}</p>

<p> if i want to comit my update to github :</p>
<p> i should use git add . </p>
<p> then git commit -m "add my message" </p>
<p> then < git push > </p>

<h1> heer is an array</h1>

<table border="2">
    <tr>

            {% for names in names %}
           <tr><td> {{names}} </td></tr>
        {% endfor %}
</tr>

</table>

</html>