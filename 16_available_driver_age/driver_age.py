# -*- encoding: utf-8 -*-
import pycountry

'''
나이를 입력 받아 미국법상 운전 가능한 나이인 16세와 비교하여 16세 이상이면
"you are old enough to legally drive."라 출력하고, 16 미만이면
"you are not old enough to legally drive."라고 출력하는 프로그램을 작성하라.

출력 예
What is your age? 15
You are not old enough to legally drive.

또는 다음과 같이 작성할 수 있다.
What is your age? 35
You are old enough to legally drive.

제약 사항
* 한 개의 출력문만 사용할 것
* 3항 연산자를 사용할 것. 사용하는 프로그래밍 언어가 3항 연산자를 지원하지 않는
다면, 일반적인 if/else문을 사용할 것. 하지만 여전히 메세지를 출력하는
출력문은 한 개만 사용할 것.

도전 과제
* 0보다 작은 값을 입력하거나, 숫자가 아닌 값을 입력하면, 올바른 나이를 입력
하라는 에러 메세지를 출력해보자.
* 프로그램 로직에 운전 가늫안 나이를 코드 안에 넣는 대신 나라별 운전 가능한
연령을 조사하여 테이블로 구성한 다음, 나이와 국가를 입력받아 해당 국가에서
운전을 할 수 있는지를 출력하도록 하는 프로그램을 수정해보자.
'''


class inspect_driver(object):
    def __init__(self):
        self.counrty_num = len(pycountry.countries)
        self.countries = {"AF": "Afghanistan",
                          "AX": "Aland Islands",
                          "AL": "Albania",
                          "DZ": "Algeria",
                          "AS": "American Samoa",
                          "AD": "Andorra",
                          "AO": "Angola",
                          "AI": "Anguilla",
                          "AQ": "Antarctica",
                          "AG": "Antigua and Barbuda",
                          "AR": "Argentina",
                          "AM": "Armenia",
                          "AW": "Aruba",
                          "AU": "Australia",
                          "AT": "Austria",
                          "AZ": "Azerbaijan",
                          "BS": "Bahamas",
                          "BH": "Bahrain",
                          "BD": "Bangladesh",
                          "BB": "Barbados",
                          "BY": "Belarus",
                          "BE": "Belgium",
                          "BZ": "Belize",
                          "BJ": "Benin",
                          "BM": "Bermuda",
                          "BT": "Bhutan",
                          "BO": "Bolivia, Plurinational State of",
                          "BQ": "Bonaire, Sint Eustatius and Saba",
                          "BA": "Bosnia and Herzegovina",
                          "BW": "Botswana",
                          "BV": "Bouvet Island",
                          "BR": "Brazil",
                          "IO": "British Indian Ocean Territory",
                          "BN": "Brunei Darussalam",
                          "BG": "Bulgaria",
                          "BF": "Burkina Faso",
                          "BI": "Burundi",
                          "KH": "Cambodia",
                          "CM": "Cameroon",
                          "CA": "Canada",
                          "CV": "Cape Verde",
                          "KY": "Cayman Islands",
                          "CF": "Central African Republic",
                          "TD": "Chad",
                          "CL": "Chile",
                          "CN": "China",
                          "CX": "Christmas Island",
                          "CC": "Cocos (Keeling) Islands",
                          "CO": "Colombia",
                          "KM": "Comoros",
                          "CG": "Congo",
                          "CD": "Congo, The Democratic Republic of the",
                          "CK": "Cook Islands",
                          "CR": "Costa Rica",
                          "CI": "Côte d'Ivoire",
                          "HR": "Croatia",
                          "CU": "Cuba",
                          "CW": "Curaçao",
                          "CY": "Cyprus",
                          "CZ": "Czech Republic",
                          "DK": "Denmark",
                          "DJ": "Djibouti",
                          "DM": "Dominica",
                          "DO": "Dominican Republic",
                          "EC": "Ecuador",
                          "EG": "Egypt",
                          "SV": "El Salvador",
                          "GQ": "Equatorial Guinea",
                          "ER": "Eritrea",
                          "EE": "Estonia",
                          "ET": "Ethiopia",
                          "FK": "Falkland Islands (Malvinas)",
                          "FO": "Faroe Islands",
                          "FJ": "Fiji",
                          "FI": "Finland",
                          "FR": "France",
                          "GF": "French Guiana",
                          "PF": "French Polynesia",
                          "TF": "French Southern Territories",
                          "GA": "Gabon",
                          "GM": "Gambia",
                          "GE": "Georgia",
                          "DE": "Germany",
                          "GH": "Ghana",
                          "GI": "Gibraltar",
                          "GR": "Greece",
                          "GL": "Greenland",
                          "GD": "Grenada",
                          "GP": "Guadeloupe",
                          "GU": "Guam",
                          "GT": "Guatemala",
                          "GG": "Guernsey",
                          "GN": "Guinea",
                          "GW": "Guinea-Bissau",
                          "GY": "Guyana",
                          "HT": "Haiti",
                          "HM": "Heard Island and McDonald Islands",
                          "VA": "Holy See (Vatican City State)",
                          "HN": "Honduras",
                          "HK": "Hong Kong",
                          "HU": "Hungary",
                          "IS": "Iceland",
                          "IN": "India",
                          "ID": "Indonesia",
                          "IR": "Iran, Islamic Republic of",
                          "IQ": "Iraq",
                          "IE": "Ireland",
                          "IM": "Isle of Man",
                          "IL": "Israel",
                          "IT": "Italy",
                          "JM": "Jamaica",
                          "JP": "Japan",
                          "JE": "Jersey",
                          "JO": "Jordan",
                          "KZ": "Kazakhstan",
                          "KE": "Kenya",
                          "KI": "Kiribati",
                          "KP": "Korea, Democratic People's Republic of",
                          "KR": "Korea, Republic of",
                          "KW": "Kuwait",
                          "KG": "Kyrgyzstan",
                          "LA": "Lao People's Democratic Republic",
                          "LV": "Latvia",
                          "LB": "Lebanon",
                          "LS": "Lesotho",
                          "LR": "Liberia",
                          "LY": "Libya",
                          "LI": "Liechtenstein",
                          "LT": "Lithuania",
                          "LU": "Luxembourg",
                          "MO": "Macao",
                          "MK": "Macedonia, Republic of",
                          "MG": "Madagascar",
                          "MW": "Malawi",
                          "MY": "Malaysia",
                          "MV": "Maldives",
                          "ML": "Mali",
                          "MT": "Malta",
                          "MH": "Marshall Islands",
                          "MQ": "Martinique",
                          "MR": "Mauritania",
                          "MU": "Mauritius",
                          "YT": "Mayotte",
                          "MX": "Mexico",
                          "FM": "Micronesia, Federated States of",
                          "MD": "Moldova, Republic of",
                          "MC": "Monaco",
                          "MN": "Mongolia",
                          "ME": "Montenegro",
                          "MS": "Montserrat",
                          "MA": "Morocco",
                          "MZ": "Mozambique",
                          "MM": "Myanmar",
                          "NA": "Namibia",
                          "NR": "Nauru",
                          "NP": "Nepal",
                          "NL": "Netherlands",
                          "NC": "New Caledonia",
                          "NZ": "New Zealand",
                          "NI": "Nicaragua",
                          "NE": "Niger",
                          "NG": "Nigeria",
                          "NU": "Niue",
                          "NF": "Norfolk Island",
                          "MP": "Northern Mariana Islands",
                          "NO": "Norway",
                          "OM": "Oman",
                          "PK": "Pakistan",
                          "PW": "Palau",
                          "PS": "Palestinian Territory, Occupied",
                          "PA": "Panama",
                          "PG": "Papua New Guinea",
                          "PY": "Paraguay",
                          "PE": "Peru",
                          "PH": "Philippines",
                          "PN": "Pitcairn",
                          "PL": "Poland",
                          "PT": "Portugal",
                          "PR": "Puerto Rico",
                          "QA": "Qatar",
                          "RE": "Réunion",
                          "RO": "Romania",
                          "RU": "Russian Federation",
                          "RW": "Rwanda",
                          "BL": "Saint Barthélemy",
                          "SH": "Saint Helena, Ascension and Tristan da Cunha",
                          "KN": "Saint Kitts and Nevis",
                          "LC": "Saint Lucia",
                          "MF": "Saint Martin (French part)",
                          "PM": "Saint Pierre and Miquelon",
                          "VC": "Saint Vincent and the Grenadines",
                          "WS": "Samoa",
                          "SM": "San Marino",
                          "ST": "Sao Tome and Principe",
                          "SA": "Saudi Arabia",
                          "SN": "Senegal",
                          "RS": "Serbia",
                          "SC": "Seychelles",
                          "SL": "Sierra Leone",
                          "SG": "Singapore",
                          "SX": "Sint Maarten (Dutch part)",
                          "SK": "Slovakia",
                          "SI": "Slovenia",
                          "SB": "Solomon Islands",
                          "SO": "Somalia",
                          "ZA": "South Africa",
                          "GS": "South Georgia and the South Sandwich Islands",
                          "ES": "Spain",
                          "LK": "Sri Lanka",
                          "SD": "Sudan",
                          "SR": "Suriname",
                          "SS": "South Sudan",
                          "SJ": "Svalbard and Jan Mayen",
                          "SZ": "Swaziland",
                          "SE": "Sweden",
                          "CH": "Switzerland",
                          "SY": "Syrian Arab Republic",
                          "TW": "Taiwan, Province of China",
                          "TJ": "Tajikistan",
                          "TZ": "Tanzania, United Republic of",
                          "TH": "Thailand",
                          "TL": "Timor-Leste",
                          "TG": "Togo",
                          "TK": "Tokelau",
                          "TO": "Tonga",
                          "TT": "Trinidad and Tobago",
                          "TN": "Tunisia",
                          "TR": "Turkey",
                          "TM": "Turkmenistan",
                          "TC": "Turks and Caicos Islands",
                          "TV": "Tuvalu",
                          "UG": "Uganda",
                          "UA": "Ukraine",
                          "AE": "United Arab Emirates",
                          "GB": "United Kingdom",
                          "US": "United States",
                          "UM": "United States Minor Outlying Islands",
                          "UY": "Uruguay",
                          "UZ": "Uzbekistan",
                          "VU": "Vanuatu",
                          "VE": "Venezuela, Bolivarian Republic of",
                          "VN": "Viet Nam",
                          "VG": "Virgin Islands, British",
                          "VI": "Virgin Islands, U.S.",
                          "WF": "Wallis and Futuna",
                          "EH": "Western Sahara",
                          "YE": "Yemen",
                          "ZM": "Zambia",
                          "ZW": "Zimbabwe"}

    def ask_driver_info(self):
        answer = ""
        age = raw_input("What is your age? ")
        country = raw_input("What is your country? ")
        self._validate_age(age)
        self._validate_country(country)
        legal_age = self.get_legal_age(country)

        if (age >= legal_age):
            answer = "You are old enough to legally drive."
        else:
            answer = "You are not old enough to legally drive."

        print(answer)

    def _validate_age(self, age):
        is_validate = True if age > 0 else False
        if not is_validate:
            assert False
        return is_validate

    def _validate_country(self, country):
        shortname_countries = self.countries.values()
        is_validate = True if country in shortname_countries else False
        if not is_validate:
            assert False
        return is_validate

    def get_legal_age(self, country):
        ret_dict = {}
        with open("./driver_age_country.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                tmp_list = line.split("\t")
                ret_dict[tmp_list[0]] = tmp_list[1]

        return ret_dict[country] if country in self.countries.keys() else None

if __name__ == "__main__":
    a = inspect_driver()
    a.ask_driver_info()


