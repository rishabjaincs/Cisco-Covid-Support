import requests
import json
import flask
from flask import request,jsonify

state_list={'Maharashtra': ['Achalpur', 'Ahmednagar', 'Akola', 'Akot', 'Amalner', 'Ambejogai', 'Amravati', 'Anjangaon', 'Arvi', 'Aurangabad', 'Bhiwandi', 'Dhule', 'Ichalkaranji', 'Kalyan-Dombivali', 'Karjat', 'Latur', 'Loha', 'Lonar', 'Lonavla', 'Mahad', 'Malegaon', 'Malkapur', 'Mangalvedhe', 'Mangrulpir', 'Manjlegaon', 'Manmad', 'Manwath', 'Mehkar', 'Mhaswad', 'Mira-Bhayandar', 'Morshi', 'Mukhed', 'Mul', 'Mumbai', 'Murtijapur', 'Nagpur', 'Nanded-Waghala', 'Nandgaon', 'Nandura', 'Nandurbar', 'Narkhed', 'Nashik', 'Nawapur', 'Nilanga', 'Osmanabad', 'Ozar', 'Pachora', 'Paithan', 'Palghar', 'Pandharkaoda', 'Pandharpur', 'Panvel', 'Parbhani', 'Parli', 'Partur', 'Pathardi', 'Pathri', 'Patur', 'Pauni', 'Pen', 'Phaltan', 'Pulgaon', 'Pune', 'Purna', 'Pusad', 'Rahuri', 'Rajura', 'Ramtek', 'Ratnagiri', 'Raver', 'Risod', 'Sailu', 'Sangamner', 'Sangli', 'Sangole', 'Sasvad', 'Satana', 'Satara', 'Savner', 'Sawantwadi', 'Shahade', 'Shegaon', 'Shendurjana', 'Shirdi', 'Shirpur-Warwade', 'Shirur', 'Shrigonda', 'Shrirampur', 'Sillod', 'Sinnar', 'Solapur', 'Soyagaon', 'Talegaon Dabhade', 'Talode', 'Tasgaon', 'Thane', 'Tirora', 'Tuljapur', 'Tumsar', 'Uchgaon', 'Udgir', 'Umarga', 'Umarkhed', 'Umred', 'Uran', 'Uran Islampur', 'Vadgaon Kasba', 'Vaijapur', 'Vasai-Virar', 'Vita', 'Wadgaon Road', 'Wai', 'Wani', 'Wardha', 'Warora', 'Warud', 'Washim', 'Yavatmal', 'Yawal', 'Yevla'], 'Delhi': ['Delhi', 'New Delhi'], 'Karnataka': ['Adyar', 'Afzalpur', 'Arsikere', 'Athni', 'Ballari', 'Belagavi', 'Bengaluru', 'Chikkamagaluru', 'Davanagere', 'Gokak', 'Hubli-Dharwad', 'Karwar', 'Kolar', 'Lakshmeshwar', 'Lingsugur', 'Maddur', 'Madhugiri', 'Madikeri', 'Magadi', 'Mahalingapura', 'Malavalli', 'Malur', 'Mandya', 'Mangaluru', 'Manvi', 'Mudabidri', 'Mudalagi', 'Muddebihal', 'Mudhol', 'Mulbagal', 'Mundargi', 'Mysore', 'Nanjangud', 'Nargund', 'Navalgund', 'Nelamangala', 'Pavagada', 'Piriyapatna', 'Puttur', 'Raayachuru', 'Rabkavi Banhatti', 'Ramanagaram', 'Ramdurg', 'Ranebennuru', 'Ranibennur', 'Robertson Pet', 'Ron', 'Sadalagi', 'Sagara', 'Sakaleshapura', 'Sanduru', 'Sankeshwara', 'Saundatti-Yellamma', 'Savanur', 'Sedam', 'Shahabad', 'Shahpur', 'Shiggaon', 'Shikaripur', 'Shivamogga', 'Shrirangapattana', 'Sidlaghatta', 'Sindagi', 'Sindhagi', 'Sindhnur', 'Sira', 'Sirsi', 'Siruguppa', 'Srinivaspur', 'Surapura', 'Talikota', 'Tarikere', 'Tekkalakote', 'Terdal', 'Tiptur', 'Tumkur', 'Udupi', 'Vijayapura', 'Wadi', 'Yadgir'], 'Gujarat': ['Adalaj', 'Ahmedabad', 'Amreli', 'Anand', 'Anjar', 'Ankleshwar', 'Bharuch', 'Bhavnagar', 'Bhuj', 'Chhapra', 'Deesa', 'Dhoraji', 'Gandhinagar', 'Godhra', 'Jamnagar', 'Kadi', 'Kapadvanj', 'Keshod', 'Khambhat', 'Lathi', 'Limbdi', 'Lunawada', 'Mahemdabad', 'Mahesana', 'Mahuva', 'Manavadar', 'Mandvi', 'Mangrol', 'Mansa', 'Modasa', 'Morvi', 'Nadiad', 'Navsari', 'Padra', 'Palanpur', 'Palitana', 'Pardi', 'Patan', 'Petlad', 'Porbandar', 'Radhanpur', 'Rajkot', 'Rajpipla', 'Rajula', 'Ranavav', 'Rapar', 'Salaya', 'Sanand', 'Savarkundla', 'Sidhpur', 'Sihor', 'Songadh', 'Surat', 'Talaja', 'Thangadh', 'Tharad', 'Umbergaon', 'Umreth', 'Una', 'Unjha', 'Upleta', 'Vadnagar', 'Vadodara', 'Valsad', 'Vapi', 'Vapi', 'Veraval', 'Vijapur', 'Viramgam', 'Visnagar', 'Vyara', 'Wadhwan', 'Wankaner'], 'Telangana': ['Adilabad', 'Bellampalle', 'Bhadrachalam', 'Bhainsa', 'Bhongir', 'Bodhan', 'Farooqnagar', 'Gadwal', 'Hyderabad', 'Jagtial', 'Jangaon', 'Kagaznagar', 'Kamareddy', 'Karimnagar', 'Khammam', 'Koratla', 'Kothagudem', 'Kyathampalle', 'Mahbubnagar', 'Mancherial', 'Mandamarri', 'Manuguru', 'Medak', 'Miryalaguda', 'Nagarkurnool', 'Narayanpet', 'Nirmal', 'Nizamabad', 'Palwancha', 'Ramagundam', 'Sadasivpet', 'Sangareddy', 'Siddipet', 'Sircilla', 'Suryapet', 'Tandur', 'Vikarabad', 'Wanaparthy', 'Warangal', 'Yellandu'], 'Tamil Nadu': ['Arakkonam', 'Aruppukkottai', 'Chennai', 'Coimbatore', 'Erode', 'Gobichettipalayam', 'Kancheepuram', 'Karur', 'Lalgudi', 'Madurai', 'Manachanallur', 'Nagapattinam', 'Nagercoil', 'Namagiripettai', 'Namakkal', 'Nandivaram-Guduvancheri', 'Nanjikottai', 'Natham', 'Nellikuppam', 'Neyveli (TS)', "O\\' Valley", 'Oddanchatram', 'P.N.Patti', 'Pacode', 'Padmanabhapuram', 'Palani', 'Palladam', 'Pallapatti', 'Pallikonda', 'Panagudi', 'Panruti', 'Paramakudi', 'Parangipettai', 'Pattukkottai', 'Perambalur', 'Peravurani', 'Periyakulam', 'Periyasemur', 'Pernampattu', 'Pollachi', 'Polur', 'Ponneri', 'Pudukkottai', 'Pudupattinam', 'Puliyankudi', 'Punjaipugalur', 'Rajapalayam', 'Ramanathapuram', 'Rameshwaram', 'Ranipet', 'Rasipuram', 'Salem', 'Sankarankovil', 'Sankari', 'Sathyamangalam', 'Sattur', 'Shenkottai', 'Sholavandan', 'Sholingur', 'Sirkali', 'Sivaganga', 'Sivagiri', 'Sivakasi', 'Srivilliputhur', 'Surandai', 'Suriyampalayam', 'Tenkasi', 'Thammampatti', 'Thanjavur', 'Tharamangalam', 'Tharangambadi', 'Theni Allinagaram', 'Thirumangalam', 'Thirupuvanam', 'Thiruthuraipoondi', 'Thiruvallur', 'Thiruvarur', 'Thuraiyur', 'Tindivanam', 'Tiruchendur', 'Tiruchengode', 'Tiruchirappalli', 'Tirukalukundram', 'Tirukkoyilur', 'Tirunelveli', 'Tirupathur', 'Tirupathur', 'Tiruppur', 'Tiruttani', 'Tiruvannamalai', 'Tiruvethipuram', 'Tittakudi', 'Udhagamandalam', 'Udumalaipettai', 'Unnamalaikadai', 'Usilampatti', 'Uthamapalayam', 'Uthiramerur', 'Vadakkuvalliyur', 'Vadalur', 'Vadipatti', 'Valparai', 'Vandavasi', 'Vaniyambadi', 'Vedaranyam', 'Vellakoil', 'Vellore', 'Vikramasingapuram', 'Viluppuram', 'Virudhachalam', 'Virudhunagar', 'Viswanatham'], 'West Bengal': ['Adra', 'AlipurdUrban Agglomerationr', 'Arambagh', 'Asansol', 'Baharampur', 'Balurghat', 'Bankura', 'Darjiling', 'English Bazar', 'Gangarampur', 'Habra', 'Hugli-Chinsurah', 'Jalpaiguri', 'Jhargram', 'Kalimpong', 'Kharagpur', 'Kolkata', 'Mainaguri', 'Malda', 'Mathabhanga', 'Medinipur', 'Memari', 'Monoharpur', 'Murshidabad', 'Nabadwip', 'Naihati', 'Panchla', 'PandUrban Agglomeration', 'Paschim Punropara', 'Purulia', 'Raghunathganj', 'Raghunathpur', 'Raiganj', 'Rampurhat', 'Ranaghat', 'Sainthia', 'Santipur', 'Siliguri', 'Sonamukhi', 'Srirampore', 'Suri', 'Taki', 'Tamluk', 'Tarakeswar'], 'Rajasthan': ['Ajmer', 'Alwar', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Jaipur', 'Jodhpur', 'Kota', 'Lachhmangarh', 'Ladnu', 'Lakheri', 'Lalsot', 'Losal', 'Makrana', 'Malpura', 'Mandalgarh', 'Mandawa', 'Mangrol', 'Merta City', 'Mount Abu', 'Nadbai', 'Nagar', 'Nagaur', 'Nasirabad', 'Nathdwara', 'Neem-Ka-Thana', 'Nimbahera', 'Nohar', 'Nokha', 'Pali', 'Phalodi', 'Phulera', 'Pilani', 'Pilibanga', 'Pindwara', 'Pipar City', 'Prantij', 'Pratapgarh', 'Raisinghnagar', 'Rajakhera', 'Rajaldesar', 'Rajgarh (Alwar)', 'Rajgarh (Churu)', 'Rajsamand', 'Ramganj Mandi', 'Ramngarh', 'Ratangarh', 'Rawatbhata', 'Rawatsar', 'Reengus', 'Sadri', 'Sadulpur', 'Sadulshahar', 'Sagwara', 'Sambhar', 'Sanchore', 'Sangaria', 'Sardarshahar', 'Sawai Madhopur', 'Shahpura', 'Shahpura', 'Sheoganj', 'Sikar', 'Sirohi', 'Sojat', 'Sri Madhopur', 'Sujangarh', 'Sumerpur', 'Suratgarh', 'Takhatgarh', 'Taranagar', 'Todabhim', 'Todaraisingh', 'Tonk', 'Udaipur', 'Udaipurwati', 'Vijainagar, Ajmer'], 'Uttar Pradesh': ['Achhnera', 'Agra', 'Aligarh', 'Allahabad', 'Amroha', 'Azamgarh', 'Bahraich', 'Chandausi', 'Etawah', 'Fatehpur Sikri', 'Firozabad', 'Hapur', 'Hardoi ', 'Jhansi', 'Kalpi', 'Kanpur', 'Khair', 'Laharpur', 'Lakhimpur', 'Lal Gopalganj Nindaura', 'Lalganj', 'Lalitpur', 'Lar', 'Loni', 'Lucknow', 'Mathura', 'Meerut', 'Mirzapur', 'Modinagar', 'Moradabad', 'Nagina', 'Najibabad', 'Nakur', 'Nanpara', 'Naraura', 'Naugawan Sadat', 'Nautanwa', 'Nawabganj', 'Nehtaur', 'Niwai', 'Noida', 'Noorpur', 'Obra', 'Orai', 'Padrauna', 'Palia Kalan', 'Parasi', 'Phulpur', 'Pihani', 'Pilibhit', 'Pilkhuwa', 'Powayan', 'Pukhrayan', 'Puranpur', 'PurqUrban Agglomerationzi', 'Purwa', 'Rae Bareli', 'Rampur', 'Rampur Maniharan', 'Rasra', 'Rath', 'Renukoot', 'Reoti', 'Robertsganj', 'Rudauli', 'Rudrapur', 'SUrban Agglomerationr', 'Sadabad', 'Safipur', 'Saharanpur', 'Sahaspur', 'Sahaswan', 'Sahawar', 'Sahjanwa', 'Saidpur', 'Sambhal', 'Samdhan', 'Samthar', 'Sandi', 'Sandila', 'Sardhana', 'Seohara', 'Shahabad, Hardoi', 'Shahabad, Rampur', 'Shahganj', 'Shahjahanpur', 'Shamli', 'Shamsabad, Agra', 'Shamsabad, Farrukhabad', 'Sherkot', 'Shikarpur, Bulandshahr', 'Shikohabad', 'Shishgarh', 'Siana', 'Sikanderpur', 'Sikandra Rao', 'Sikandrabad', 'Sirsaganj', 'Sirsi', 'Sitapur', 'Soron', 'Sultanpur', 'Sumerpur', 'Tanda', 'Thakurdwara', 'Thana Bhawan', 'Tilhar', 'Tirwaganj', 'Tulsipur', 'Tundla', 'Ujhani', 'Unnao', 'Utraula', 'Varanasi', 'Vrindavan', 'Warhapur', 'Zaidpur', 'Zamania'], 'Bihar': ['Araria', 'Arrah', 'Arwal', 'Asarganj', 'Aurangabad', 'Bagaha', 'Barh', 'Begusarai', 'Bettiah', 'BhabUrban Agglomeration', 'Bhagalpur', 'Buxar', 'Chhapra', 'Darbhanga', 'Dehri-on-Sone', 'Dumraon', 'Forbesganj', 'Gaya', 'Gopalganj', 'Hajipur', 'Jamalpur', 'Jamui', 'Jehanabad', 'Katihar', 'Kishanganj', 'Lakhisarai', 'Lalganj', 'Madhepura', 'Madhubani', 'Maharajganj', 'Mahnar Bazar', 'Makhdumpur', 'Maner', 'Manihari', 'Marhaura', 'Masaurhi', 'Mirganj', 'Mokameh', 'Motihari', 'Motipur', 'Munger', 'Murliganj', 'Muzaffarpur', 'Narkatiaganj', 'Naugachhia', 'Nawada', 'Nokha', 'Patna', 'Piro', 'Purnia', 'Rafiganj', 'Rajgir', 'Ramnagar', 'Raxaul Bazar', 'Revelganj', 'Rosera', 'Saharsa', 'Samastipur', 'Sasaram', 'Sheikhpura', 'Sheohar', 'Sherghati', 'Silao', 'Sitamarhi', 'Siwan', 'Sonepur', 'Sugauli', 'Sultanganj', 'Supaul', 'Warisaliganj'], 'Madhya Pradesh': ['Alirajpur', 'Ashok Nagar', 'Balaghat', 'Bhopal', 'Ganjbasoda', 'Gwalior', 'Indore', 'Itarsi', 'Jabalpur', 'Lahar', 'Maharajpur', 'Mahidpur', 'Maihar', 'Malaj Khand', 'Manasa', 'Manawar', 'Mandideep', 'Mandla', 'Mandsaur', 'Mauganj', 'Mhow Cantonment', 'Mhowgaon', 'Morena', 'Multai', 'Mundi', 'Murwara (Katni)', 'Nagda', 'Nainpur', 'Narsinghgarh', 'Narsinghgarh', 'Neemuch', 'Nepanagar', 'Niwari', 'Nowgong', 'Nowrozabad (Khodargama)', 'Pachore', 'Pali', 'Panagar', 'Pandhurna', 'Panna', 'Pasan', 'Pipariya', 'Pithampur', 'Porsa', 'Prithvipur', 'Raghogarh-Vijaypur', 'Rahatgarh', 'Raisen', 'Rajgarh', 'Ratlam', 'Rau', 'Rehli', 'Rewa', 'Sabalgarh', 'Sagar', 'Sanawad', 'Sarangpur', 'Sarni', 'Satna', 'Sausar', 'Sehore', 'Sendhwa', 'Seoni', 'Seoni-Malwa', 'Shahdol', 'Shajapur', 'Shamgarh', 'Sheopur', 'Shivpuri', 'Shujalpur', 'Sidhi', 'Sihora', 'Singrauli', 'Sironj', 'Sohagpur', 'Tarana', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha', 'Vijaypur', 'Wara Seoni'], 'Andhra Pradesh': ['Adoni', 'Amalapuram', 'Anakapalle', 'Anantapur', 'Bapatla', 'Bheemunipatnam', 'Bhimavaram', 'Bobbili', 'Chilakaluripet', 'Chirala', 'Chittoor', 'Dharmavaram', 'Eluru', 'Gooty', 'Gudivada', 'Gudur', 'Guntakal', 'Guntur', 'Hindupur', 'Jaggaiahpet', 'Jammalamadugu', 'Kadapa', 'Kadiri', 'Kakinada', 'Kandukur', 'Kavali', 'Kovvur', 'Kurnool', 'Macherla', 'Machilipatnam', 'Madanapalle', 'Mandapeta', 'Markapur', 'Nagari', 'Naidupet', 'Nandyal', 'Narasapuram', 'Narasaraopet', 'Narsipatnam', 'Nellore', 'Nidadavole', 'Nuzvid', 'Ongole', 'Palacole', 'Palasa Kasibugga', 'Parvathipuram', 'Pedana', 'Peddapuram', 'Pithapuram', 'Ponnur', 'Proddatur', 'Punganur', 'Puttur', 'Rajahmundry', 'Rajam', 'Rajampet', 'Ramachandrapuram', 'Rayachoti', 'Rayadurg', 'Renigunta', 'Repalle', 'Salur', 'Samalkot', 'Sattenapalle', 'Srikakulam', 'Srikalahasti', 'Srisailam Project (Right Flank Colony) Township', 'Sullurpeta', 'Tadepalligudem', 'Tadpatri', 'Tanuku', 'Tenali', 'Tirupati', 'Tiruvuru', 'Tuni', 'Uravakonda', 'Venkatagiri', 'Vijayawada', 'Vinukonda', 'Visakhapatnam', 'Vizianagaram', 'Yemmiganur', 'Yerraguntla'], 'Punjab': ['Amritsar', 'Barnala', 'Batala', 'Bathinda', 'Dhuri', 'Faridkot', 'Fazilka', 'Firozpur', 'Firozpur Cantt.', 'Gobindgarh', 'Gurdaspur', 'Hoshiarpur', 'Jagraon', 'Jalandhar', 'Jalandhar Cantt.', 'Kapurthala', 'Khanna', 'Kharar', 'Kot Kapura', 'Longowal', 'Ludhiana', 'Malerkotla', 'Malout', 'Mansa', 'Moga', 'Mohali', 'Morinda, India', 'Mukerian', 'Muktsar', 'Nabha', 'Nakodar', 'Nangal', 'Nawanshahr', 'Pathankot', 'Patiala', 'Patti', 'Pattran', 'Phagwara', 'Phillaur', 'Qadian', 'Raikot', 'Rajpura', 'Rampura Phul', 'Rupnagar', 'Samana', 'Sangrur', 'Sirhind Fatehgarh Sahib', 'Sujanpur', 'Sunam', 'Talwara', 'Tarn Taran', 'Urmar Tanda', 'Zira', 'Zirakpur'], 'Haryana': ['Bahadurgarh', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gohana', 'Gurgaon', 'Hansi', 'Hisar', 'Jind', 'Kaithal', 'Karnal', 'Ladwa', 'Mahendragarh', 'Mandi Dabwali', 'Narnaul', 'Narwana', 'Palwal', 'Panchkula', 'Panipat', 'Pehowa', 'Pinjore', 'Rania', 'Ratia', 'Rewari', 'Rohtak', 'Safidon', 'Samalkha', 'Sarsod', 'Shahbad', 'Sirsa', 'Sohna', 'Sonipat', 'Taraori', 'Thanesar', 'Tohana', 'Yamunanagar'], 'Jammu and Kashmir': ['Anantnag', 'Baramula', 'Jammu', 'KathUrban Agglomeration', 'Punch', 'Rajauri', 'Sopore', 'Srinagar', 'Udhampur'], 'Jharkhand': ['Adityapur', 'Bokaro Steel City', 'Chaibasa', 'Chatra', 'Chirkunda', 'Deoghar', 'Dhanbad', 'Dumka', 'Giridih', 'Gumia', 'Hazaribag', 'Jamshedpur', 'Jhumri Tilaiya', 'Lohardaga', 'Madhupur', 'Medininagar (Daltonganj)', 'Mihijam', 'Musabani', 'Pakaur', 'Patratu', 'Phusro', 'Ramgarh', 'Ranchi', 'Sahibganj', 'Saunda', 'Simdega', 'Tenu dam-cum-Kathhara'], 'Chhattisgarh': ['Ambikapur', 'Bhatapara', 'Bhilai Nagar', 'Bilaspur', 'Chirmiri', 'Dalli-Rajhara', 'Dhamtari', 'Durg', 'Jagdalpur', 'Korba', 'Mahasamund', 'Manendragarh', 'Mungeli', 'Naila Janjgir', 'Raigarh', 'Raipur', 'Rajnandgaon', 'Sakti', 'Tilda Newra'], 'Assam': ['Barpeta', 'Bongaigaon City', 'Dhubri', 'Dibrugarh', 'Diphu', 'Dispur', 'Goalpara', 'Guwahati', 'Jorhat', 'Karimganj', 'Lanka', 'Lumding', 'Mangaldoi', 'Mankachar', 'Margherita', 'Mariani', 'Marigaon', 'Nagaon', 'Nalbari', 'North Lakhimpur', 'Rangia', 'Sibsagar', 'Silapathar', 'Silchar', 'Tezpur', 'Tinsukia'], 'Chandigarh': ['Chandigarh'], 'Odisha': ['Balangir', 'Baleshwar Town', 'Barbil', 'Bargarh', 'Baripada Town', 'Bhadrak', 'Bhawanipatna', 'Bhubaneswar', 'Brahmapur', 'Byasanagar', 'Cuttack', 'Dhenkanal', 'Jatani', 'Jharsuguda', 'Kendrapara', 'Kendujhar', 'Malkangiri', 'Nabarangapur', 'Paradip', 'Parlakhemundi', 'Pattamundai', 'Phulabani', 'Puri', 'Rairangpur', 'Rajagangapur', 'Raurkela', 'Rayagada', 'Sambalpur', 'Soro', 'Sunabeda', 'Sundargarh', 'Talcher', 'Tarbha', 'Titlagarh'], 'Kerala': ['Adoor', 'Alappuzha', 'Attingal', 'Chalakudy', 'Changanassery', 'Cherthala', 'Chittur-Thathamangalam', 'Guruvayoor', 'Kanhangad', 'Kannur', 'Kasaragod', 'Kayamkulam', 'Kochi', 'Kodungallur', 'Kollam', 'Kottayam', 'Koyilandy', 'Kozhikode', 'Kunnamkulam', 'Malappuram', 'Mattannur', 'Mavelikkara', 'Mavoor', 'Muvattupuzha', 'Nedumangad', 'Neyyattinkara', 'Nilambur', 'Ottappalam', 'Palai', 'Palakkad', 'Panamattom', 'Panniyannur', 'Pappinisseri', 'Paravoor', 'Pathanamthitta', 'Peringathur', 'Perinthalmanna', 'Perumbavoor', 'Ponnani', 'Punalur', 'Puthuppally', 'Shoranur', 'Taliparamba', 'Thiruvalla', 'Thiruvananthapuram', 'Thodupuzha', 'Thrissur', 'Tirur', 'Vaikom', 'Varkala', 'Vatakara'], 'Uttarakhand': ['Bageshwar', 'Dehradun', 'Haldwani-cum-Kathgodam', 'Hardwar', 'Kashipur', 'Manglaur', 'Mussoorie', 'Nagla', 'Nainital', 'Pauri', 'Pithoragarh', 'Ramnagar', 'Rishikesh', 'Roorkee', 'Rudrapur', 'Sitarganj', 'Srinagar', 'Tehri'], 'Puducherry': ['Karaikal', 'Mahe', 'Pondicherry', 'Yanam'], 'Tripura': ['Agartala', 'Belonia', 'Dharmanagar', 'Kailasahar', 'Khowai', 'Pratapgarh', 'Udaipur'], 'Mizoram': ['Aizawl', 'Lunglei', 'Saiha'], 'Meghalaya': ['Nongstoin', 'Shillong', 'Tura'], 'Manipur': ['Imphal', 'Lilong', 'Mayang Imphal', 'Thoubal'], 'Himachal Pradesh': ['Kullu', 'Manali', 'Mandi', 'Nahan', 'Palampur', 'Shimla', 'Solan', 'Sundarnagar'], 'Nagaland': ['Dimapur', 'Kohima', 'Mokokchung', 'Tuensang', 'Wokha', 'Zunheboto'], 'Goa': ['Mapusa', 'Margao', 'Marmagao', 'Panaji'], 'Andaman and Nicobar Islands': ['Port Blair'], 'Arunachal Pradesh': ['Naharlagun', 'Pasighat'], 'Dadra and Nagar Haveli': ['Silvassa']}

def body_frame(cityMap,state):
    body={
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "width": 80,
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Cisco Covid Support",
                                "wrap": True,
                                "horizontalAlignment": "Center",
                                "size": "ExtraLarge",
                                "weight": "Lighter",
                                "color": "Accent",
                                "isSubtle": True,
                                "separator": True
                            }
                        ]
                    }
                ]
            },
            {
                "type": "Container"
            },
            {
                "type": "Input.ChoiceSet",
                "choices": cityMap,
                "placeholder": "Select the City",
                "id": "city"
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "PIN Code",
                                "wrap": True,
                                "color": "Dark",
                                "weight": "Bolder",
                                "fontType": "Default",
                                "isSubtle": True
                            }
                        ],
                        "verticalContentAlignment": "Center",
                        "width": 20
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Input.Text",
                                "placeholder": "560001",
                                "id": "pincode",
                                "maxLength": 6
                            }
                        ],
                        "width": 80
                    }
                ]
            },
            {
                "type": "ActionSet",
                "actions": [
                    {
                        "type": "Action.ShowCard",
                        "title": "GET Information",
                        "card": {
                            "type": "AdaptiveCard",
                            "body": [
                                {
                                    "type": "TextBlock",
                                    "text": "Fill in below details to get better visibility from community",
                                    "wrap": True,
                                    "isSubtle": True
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": 100,
                                            "items": [
                                                {
                                                    "type": "Input.ChoiceSet",
                                                    "choices": [{'title': 'Ambulance Services', 'value': 'Ambulance Services'},
                                                    {'title': 'Blood and Plasma', 'value': 'Blood and Plasma'},
                                                    {'title': 'Doctor Consultation', 'value': 'Doctor Consultation'},
                                                    {'title': 'Home Care and Covid Support Package',
                                                    'value': 'Home Care and Covid Support Package'},
                                                    {'title': 'Hospital Beds-CovidCareCentre',
                                                    'value': 'Hospital Beds-CovidCareCentre'},
                                                    {'title': 'Hospital Beds-ICU', 'value': 'Hospital Beds-ICU'},
                                                    {'title': 'Hospital Beds-NormalBed', 'value': 'Hospital Beds-NormalBed'},
                                                    {'title': 'Hospital Beds-OxegenBed', 'value': 'Hospital Beds-OxegenBed'},
                                                    {'title': 'Medicine', 'value': 'Medicine'},
                                                    {'title': 'Other', 'value': 'Other'},
                                                    {'title': 'Oxygen', 'value': 'Oxygen'},
                                                    {'title': 'Quarantine Centre', 'value': 'Quarantine Centre'},
                                                    {'title': 'Ventilator', 'value': 'Ventilator'}],
                                                    "placeholder": "Requirements",
                                                    "id": "req1"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Elaborate the Details to help in coordinating better",
                                    "wrap": True,
                                    "spacing": "ExtraLarge",
                                    "horizontalAlignment": "Center",
                                    "size": "Small",
                                    "color": "Light",
                                    "isSubtle": True
                                },
                                {
                                    "type": "Input.Text",
                                    "placeholder": "Enter the details here",
                                    "isMultiline": True,
                                    "separator": True,
                                    "id": "RequestElaborate"
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": 30,
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Severity",
                                                    "wrap": True,
                                                    "horizontalAlignment": "Center"
                                                }
                                            ],
                                            "horizontalAlignment": "Center",
                                            "verticalContentAlignment": "Center"
                                        },
                                        {
                                            "type": "Column",
                                            "width": 70,
                                            "items": [
                                                {
                                                    "type": "Input.ChoiceSet",
                                                    "choices": [
                                                        {
                                                            "title": "Emergency",
                                                            "value": "Emergency"
                                                        },
                                                        {
                                                            "title": "Critical",
                                                            "value": "Critical"
                                                        },
                                                        {
                                                            "title": "Moderate",
                                                            "value": "Moderate"
                                                        }
                                                    ],
                                                    "placeholder": "Select Severity",
                                                    "id": "sev"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.Submit",
                                            "title": "Search",
                                            "data":{"status":"request","state":state}
                                        }
                                    ],
                                    "horizontalAlignment": "Center",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    },
                    {
                        "type": "Action.ShowCard",
                        "title": "ADD Information",
                        "card": {
                            "type": "AdaptiveCard",
                            "body": [
                                {
                                    "type": "TextBlock",
                                    "text": "Fill in below details to help easy search",
                                    "wrap": True,
                                    "isSubtle": True
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": 100,
                                            "items": [
                                                {
                                                    "type": "Input.ChoiceSet",
                                                    "choices": [{'title': 'Ambulance Services', 'value': 'Ambulance Services'},
                                                    {'title': 'Blood and Plasma', 'value': 'Blood and Plasma'},
                                                    {'title': 'Doctor Consultation', 'value': 'Doctor Consultation'},
                                                    {'title': 'Home Care and Covid Support Package',
                                                    'value': 'Home Care and Covid Support Package'},
                                                    {'title': 'Hospital Beds-CovidCareCentre',
                                                    'value': 'Hospital Beds-CovidCareCentre'},
                                                    {'title': 'Hospital Beds-ICU', 'value': 'Hospital Beds-ICU'},
                                                    {'title': 'Hospital Beds-NormalBed', 'value': 'Hospital Beds-NormalBed'},
                                                    {'title': 'Hospital Beds-OxegenBed', 'value': 'Hospital Beds-OxegenBed'},
                                                    {'title': 'Medicine', 'value': 'Medicine'},
                                                    {'title': 'Other', 'value': 'Other'},
                                                    {'title': 'Oxygen', 'value': 'Oxygen'},
                                                    {'title': 'Quarantine Centre', 'value': 'Quarantine Centre'},
                                                    {'title': 'Ventilator', 'value': 'Ventilator'}],
                                                    "placeholder": "Responses",
                                                    "id": "res1"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Elaborate the resource details",
                                    "wrap": True,
                                    "spacing": "ExtraLarge",
                                    "horizontalAlignment": "Center",
                                    "size": "Small",
                                    "color": "Light",
                                    "isSubtle": True
                                },
                                {
                                    "type": "Input.Text",
                                    "placeholder": "Enter the details",
                                    "isMultiline": True,
                                    "separator": True,
                                    "id": "resourceElaborate"
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": 40,
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Contact Person",
                                                    "wrap": True,
                                                    "horizontalAlignment": "Center"
                                                }
                                            ],
                                            "horizontalAlignment": "Center",
                                            "verticalContentAlignment": "Center"
                                        },
                                        {
                                            "type": "Column",
                                            "width": 60,
                                            "items": [
                                                {
                                                    "type": "Input.Text",
                                                    "placeholder": "John A",
                                                    "id": "contactname"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": 40,
                                            "items": [
                                                {
                                                    "type": "TextBlock",
                                                    "text": "Contact Information",
                                                    "wrap": True,
                                                    "horizontalAlignment": "Center"
                                                }
                                            ],
                                            "horizontalAlignment": "Center",
                                            "verticalContentAlignment": "Center"
                                        },
                                        {
                                            "type": "Column",
                                            "width": 60,
                                            "items": [
                                                {
                                                    "type": "Input.Text",
                                                    "placeholder": "9876543210",
                                                    "style": "Tel",
                                                    "id": "contactnumber"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "Input.Toggle",
                                                    "title": "Verified",
                                                    "id": "verified"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "Input.Toggle",
                                                    "title": "Not Verified",
                                                    "id": "notverified"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.Submit",
                                            "title": "Submit",
                                            "data":{"status":"insert","state":state}
                                        }
                                    ],
                                    "horizontalAlignment": "Center",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    },
                    {
                        "type": "Action.ShowCard",
                        "title": "Help Links",
                        "card": {
                            "type": "AdaptiveCard",
                            "body": [
                                {
                                    "type": "TextBlock",
                                    "text": "Global Support",
                                    "wrap": True
                                },
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Global",
                                            "url": "https://www.who.int/emergencies/diseases/novel-coronavirus-2019"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "India",
                                            "url": "https://www.covid19india.org/"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Vaccination",
                                            "url": "https://www.cowin.gov.in/home"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Covid Help",
                                            "url": "https://www.mohfw.gov.in/"
                                        }
                                    ],
                                    "horizontalAlignment": "Center",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Cisco Support",
                                    "wrap": True
                                },
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Quarantine",
                                            "url": "https://cisco.sharepoint.com/:w:/r/sites/PeopleCommunities-India/Cisco%20Wellbeing/India%20COVID-19%20Pandemic%20Support/Quarantine%20%26%20Isolation%20Support%20Resources/Hotel%20Quarantine%20Facility%20with%20Apollo%20Hospitals.docx?d=w11a744e1ca304ff7aa6958f4103166fe&csf=1&web=1&e=IiVlHM&CT=1620075127294&OR=Outlook-Body&CID=A299CC6E-F5FF-4714-9FC5-C625413BC067&wdLOR=c1FA74577-8D35-44BE-B482-ACDBB8F3144A"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Home Care",
                                            "url": "https://cisco.sharepoint.com/sites/PeopleCommunities-India/Cisco%20Wellbeing/Forms/AllItems.aspx?id=%2Fsites%2FPeopleCommunities%2DIndia%2FCisco%20Wellbeing%2FIndia%20COVID%2D19%20Pandemic%20Support%2FPreventive%20Support%20Resources%2FVaccination%20Support%20Service%2Epdf&parent=%2Fsites%2FPeopleCommunities%2DIndia%2FCisco%20Wellbeing%2FIndia%20COVID%2D19%20Pandemic%20Support%2FPreventive%20Support%20Resources"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Financial Assistance",
                                            "url": "https://cisco.sharepoint.com/:b:/r/sites/PeopleCommunities-India/Cisco%20Wellbeing/India%20COVID-19%20Pandemic%20Support/Additional%20Resources/FINANCIAL%20ASSISTANCE%20DURING%20COVID-19.pdf?csf=1&web=1&e=MMFhWx&CT=1620075207211&OR=Outlook-Body&CID=B4E099DD-D56E-4DB8-B58B-96A5EFBC215E&wdLOR=c86541D13-65FF-4859-8EC0-270C084D92D5"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Covid Exposure",
                                            "url": "https://app.smartsheet.com/b/form/f45a0d6dc34e4e328fcd0d85b0a9de34"
                                        },
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Pandemic Planning Site",
                                            "url": "https://cisco.sharepoint.com/sites/PeopleCommunities-India/SitePages/India-COVID-Pandemic-Support.aspx"
                                        }
                                    ],
                                    "horizontalAlignment": "Center",
                                    "spacing": "Small"
                                }
                            ]
                        }
                    }
                ],
                "horizontalAlignment": "Center"
            }
        ]
    }
    return body

def cityMapper(state):
    cityMap=[]
    for city in state_list[state]:
        cityMap.append({
                        "title": city,
                        "value": city
                    })
    return cityMap
    

def startToken(roomId,parentId,token,state):
    url="https://webexapis.com/v1/messages/{}".format(parentId)

    headers={'content-type': "application/json; charset=utf-8",
         'authorization':'Bearer {}'.format(token),
         'accept':"application/json"}

    cityMap=cityMapper(state)     
    body=body_frame(cityMap,state)

    card={
     "roomId": roomId,
      "markdown": "Token Master Form to get the Consent Response !!",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": body
        }
      ]
    }


    payload=json.dumps(card)
    response = requests.request("PUT", url, data=payload, headers=headers)
    # send_message=response.json()
    return response.status_code

