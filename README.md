# timewarrior-southamerica-holidays

Ready-to-use holidays definitions for South america countries to be loaded by timewarrior.

Download the corresponding file to your country:


COUNTRY 					|   FILE 
----------------------------|------------------
Argentina 					|	holidays.es-AR
Bolivia 					|	holidays.es-BO
Brasil						|	holidays.pt-BR
Chile 						|	holidays.es-CL
Colombia 					|	holidays.es-CO
Ecuador 					|	holidays.es-EC
Guyana  	 				|   holidays.en-GY
Paraguay 					|	holidays.es-PY
Peru 						|	holidays.es-PE
Suriname   					|   holidays.en-SR
Trinidad and Tobago 		|   holidays.en-TT
Uruguay 					|	holidays.es-UY
Venezuela 					|	holidays.es-VE
Francia(Guayana Francesa) 	|   holidays.en-FG



As mentioned in [timewarrior's tutorial - holidays](https://timewarrior.net/docs/tutorial.html#holidays), 
open the file `~/.timewarrior/timewarrior.cfg` in edition mode to add an import line indicating the location of the holidays\' file:

`import /path/to/file/holidays.en-GY`


Use  `$ timew month`  to see if there's a holiday in your country for the current month.
In the following example ran in March, the file `holidays.en-GY` (holidays for Guyana) was loaded. There's a holiday on March 29, so the output for `$ timew month` is:
!(https://raw.githubusercontent.com/rizel/timewarrior-southamerica-holidays/master/output.png)

Thanks to [public holidays global](https://publicholidays.global/) for providing the data.
