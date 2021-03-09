# timewarrior-southamerica-holidays

Ready-to-use holidays definitions for South america countries to be loaded by timewarrior.

Download the corresponding file to your country:

* Argentina 				->	holidays.es-AR
* Bolivia 					->	holidays.es-BO
* Brasil					->	holidays.pt-BR
* Chile 					->	holidays.es-CL
* Colombia 					->	holidays.es-CO
* Ecuador 					->	holidays.es-EC
* Guyana  	 				->  en-gy (missing) https://publicholidays.gy/2021-dates/
* Paraguay 					->	holidays.es-PY
* Peru 						->	holidays.es-PE
* Surinam   				->  nl-sr (missing) https://publicholidays.la/suriname/2021-dates/
* Trinidad y Tobago 		->  en-tt (missing) https://publicholidays.la/trinidad-and-tobago/2021-dates/
* Uruguay 					->	holidays.es-UY
* Venezuela 				->	holidays.es-VE
* Francia(Guayana Francesa) ->  (missing) https://publicholidays.la/french-guiana/2021-dates/



As mentioned in [timewarrior's tutorial - holidays](https://timewarrior.net/docs/tutorial.html#holidays), 
open the file `~/.timewarrior/timewarrior.cfg` in edition mode to add an import line indicating the location of the holidays\' file:

`import /path/to/file/holidays.es-BO`


Use  `$ timew month`  to see if there's a holiday in your country for the current month.

Thanks to [public holidays global](https://publicholidays.global/) for providing the data.
