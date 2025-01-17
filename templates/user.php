<!DOCTYPE html>
<html>
<h1> hello {{name}} </h1>
<p> the replas shuld be in tow {}</p>

<h1> heer is an array</h1>

<table border="2">
    <tr>

            {% for names in names %}
           <tr><td> {{names}} </td></tr>
        {% endfor %}
</tr>

</table>

</html>