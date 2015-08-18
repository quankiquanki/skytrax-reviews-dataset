# Skytrax User Reviews Dataset (August 2nd, 2015)
A scraped dataset created from all user reviews found on Skytrax (www.airlinequality.com). I could not find under which license Skytrax publishes the reviews. The reviews are accessible by anyone with a browser and the robots.txt on their website did not prohibit the scraping of them.

The reviews are divided into 4 csv files. Each file contains reviews of one category.

In total there are:
  - 41396 Airline Reviews
  - 17721 Airport Reviews
  - 1258 Seat Reviews
  - 2264 Lounge Reviews

###Airline Dataset
Total Samples: 41396

Number of Values per Column:
- (object) airline_name: 41396
- (object) link: 41396
- (object) title: 41396
- (object) author: 41396
- (object) author_country: 39805
- (object) date: 41396
- (object) content: 41396
- (object) aircraft: 1278
- (object) type_traveller: 2378
- (object) cabin_flown: 38520
- (object) route: 2341
- (float64) overall_rating: 36861
- (float64) seat_comfort_rating: 33706
- (float64) cabin_staff_rating: 33708
- (float64) food_beverages_rating: 33264
- (float64) inflight_entertainment_rating: 31114
- (float64) ground_service_rating: 2203
- (float64) wifi_connectivity_rating: 565
- (float64) value_money_rating: 39723
- (int64) recommended: 41396



###Airport Dataset
Total Samples: 17721

Number of Values per Column:
- (object) airport_name: 17721
- (object) link: 17721
- (object) title: 17721
- (object) author: 17721
- (object) author_country: 12777
- (object) date: 17721
- (object) content: 17721
- (object) experience_airport: 647
- (object) date_visit: 593
- (object) type_traveller: 646
- (float64) overall_rating: 13796
- (float64) queuing_rating: 12813
- (float64) terminal_cleanliness_rating: 12815
- (float64) terminal_seating_rating: 587
- (float64) terminal_signs_rating: 27
- (float64) food_beverages_rating: 630
- (float64) airport_shopping_rating: 12676
- (float64) wifi_connectivity_rating: 412
- (float64) airport_staff_rating: 26
- (int64) recommended: 17721



###Lounge Dataset
Total Samples: 2264

Number of Values per Column:
- (object) airline_name: 2264
- (object) link: 2264
- (object) title: 2264
- (object) author: 2264
- (object) author_country: 1783
- (object) date: 2264
- (object) content: 2264
- (object) lounge_name: 2261
- (object) airport: 2170
- (object) lounge_type: 1964
- (object) date_visit: 99
- (object) type_traveller: 119
- (float64) overall_rating: 2259
- (int64) comfort_rating: 2264
- (int64) cleanliness_rating: 2264
- (float64) bar_beverages_rating: 2259
- (float64) catering_rating: 2261
- (float64) washrooms_rating: 2238
- (float64) wifi_connectivity_rating: 2253
- (float64) staff_service_rating: 2255
- (int64) recommended: 2264



###Seat Dataset
Total Samples: 1258

Number of Values per Column:
- (object) airline_name: 1258
- (object) link: 1258
- (object) title: 1258
- (object) author: 1258
- (object) author_country: 1250
- (object) date: 1258
- (object) content: 1258
- (object) aircraft: 1258
- (object) seat_layout: 1252
- (object) date_flown: 113
- (object) cabin_flown: 1252
- (object) type_traveller: 118
- (float64) overall_rating: 1257
- (int64) seat_legroom_rating: 1258
- (int64) seat_recline_rating: 1258
- (int64) seat_width_rating: 1258
- (int64) aisle_space_rating: 1258
- (float64) viewing_tv_rating: 1229
- (float64) power_supply_rating: 62
- (float64) seat_storage_rating: 113
- (int64) recommended: 1258
