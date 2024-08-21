# listas ejercicio 2

# 1. La siguiente es una lista de 10 estudiantes de edad:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordenar la lista y encontrar la edad min y max

ages.sort()
min_ages = min(ages)
max_ages = max(ages)
print('Lista ordenada:', ages)
print('Edad minima:', min_ages)
print('Edad maxima:', max_ages)

#Añadir la edad min y la edad máxima de nuevo a la lista

ages.append(min_ages)
ages.append(max_ages)
print(ages)

#Encuentra la mediana de edad (un artículo medio o dos artículos medios divididos por dos)

ages.sort()
n = len(ages)  # Esto nos da el número de elementos
# Calcular la mediana
if n % 2 == 0:  # Si el número de elementos es par
    mediana = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:  # Si el número de elementos es impar
    mediana = ages[n // 2]

print("Mediana de edad:", mediana)


#Encontrar la edad promedio (suma de todos los artículos divididos por su número)

# Calcular la edad promedio
promedio = sum(ages) / len(ages)
print("Edad promedio:", promedio)

## Calcular el rango de las edades
rango = max_ages - min_ages
print("Rango de edades:", rango)

#Compare el valor del método (min - promedio) y (máximo - promedio), uso abs()

diferencia_min = abs(min_ages - promedio)
diferencia_max = abs(max_ages - promedio)

print("Diferencia (min - promedio):", diferencia_min)
print("Diferencia (max - promedio):", diferencia_max)

#Encuentra el país medio (es) en la lista de países

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

mid_country = len(countries) // 2
mid_country_index = mid_country - 1
print("Pais medio:", countries[mid_country_index])

#Divide la lista de los países en dos listas iguales si es aunque no sea un país más durante el primer semestre.

first_half = countries[:mid_country_index + 1]
second_half = countries[mid_country_index + 1:]

if len(first_half) != len(second_half):
    print("La lista de países no es un cuadrado.")
    

#['China', 'Russia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desempaquetar los tres primeros países y el resto como países escándádicos.

paises = ['China', 'Russia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
first_three = paises[:3]
paises_escandadicos = paises[3:] 
print("Primeros tres países:", first_three)
print("Países escandádicos:", paises_escandadicos)