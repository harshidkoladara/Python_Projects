import sqlite3
import pandas as pd


conn=sqlite3.connect("hospital.db")
c=conn.cursor()

class State(object):

	def __init__(self, id, state, country, add = True):
		c.execute(
			'''CREATE TABLE IF NOT EXISTS state (
				id int PRIMARY KEY,
				state varchar(3),
				country varchar(3)
			)'''
		)
		self.__id = id
		self.__state = state
		self.__country = country
		if add:
			c.execute("INSERT INTO state(id, state, country)  VALUES(?, ?, ?)", (id, state, country))
			conn.commit()

	def get_state(self):
		return self.__state

	def get_country(self):
		return self.__country

	def set_state(self, state):
		self.__state = state
		c.execute("UPDATE state SET state = ? WHERE id = ?", (state, self.__id))

	def set_country(self, country):
		self.__country = country
		c.execute("UPDATE state SET country = ? WHERE id = ?", (country, self.__id))



class HospitalType(object):

	def __init__(self, id, hospital_type, hospital_ownership, add=True):
		c.execute(
			'''CREATE TABLE IF NOT EXISTS hospital_type (
				id int PRIMARY KEY,
				hospital_type varchar(52),
				hospital_ownership varchar(52)
			)'''
		)
		self.__id = id
		self.__hospital_type = hospital_type
		self.__hospital_ownership = hospital_ownership
		if add:
			c.execute("INSERT INTO hospital_type (id, hospital_type, hospital_ownership) VALUES(?, ?, ?)", (id, hospital_type, hospital_ownership))
			conn.commit()


	def get_hospital_type(self):
		return self.__hospital_type

	def get_hospital_ownership(self):
		return self.__hospital_ownership

	def set_hospital_type(self, hospital_type):
		self.__hospital_type = hospital_type
		c.execute("UPDATE hospital_type SET hospital_type = ? WHERE id = ?", (hospital_type, self.__id))
		
	def set_hospital_ownership(self, hospital_ownership):
		self.__hospital_ownership = hospital_ownership
		c.execute("UPDATE hospital_type SET hospital_ownership = ? WHERE id = ?", (hospital_ownership, self.__id))


class Hospital(State, HospitalType):

	def __init__(
		self, 
		provider_id, 
		hospital_name, 
		address, 
		city, 
		state, 
		zip_code, 
		country_name, 
		phone_number, 
		hospital_type, 
		hospital_ownership, 
		emergency_services, 
		meets_criteria_for_meaningful_use_of_EHRs,
        hospital_overall_rating, 
        hospital_overall_rating_footnote,
        mortality_national_comparison,
        mortality_national_comparison_footnote,
        safety_of_care_national_comparison,
        safety_of_care_national_comparison_footnote,
        readmission_national_comparison,
        readmission_national_comparison_footnote,
        patient_experience_national_comparison,
        patient_experience_national_comparison_footnote,
        effectiveness_of_care_national_comparison,
        effectiveness_of_care_national_comparison_footnote,
        timeliness_of_care_national_comparison,
        timeliness_of_care_national_comparison_footnote,
        efficient_use_of_medical_imaging_national_comparison,
        efficient_use_of_medical_imaging_national_comparison_footnote,
        unnamed_28, 
        hospital_number_of_reviews, 
        last_review,
        reviews_per_month, 
        VIPcare_availability_365,
		add = True
        ):
		State.__init__(self, provider_id, state, country_name, add)
		HospitalType.__init__(self, provider_id, hospital_type, hospital_ownership, add)
		self.__provider_id = provider_id 
		self.__hospital_name = hospital_name 
		self.__address = address 
		self.__city = city
		self.__zip_code = zip_code
		self.__phone_number = phone_number
		self.__emergency_services = emergency_services 
		self.__meets_criteria_for_meaningful_use_of_EHRs = meets_criteria_for_meaningful_use_of_EHRs
		self.__hospital_overall_rating = hospital_overall_rating
		self.__hospital_overall_rating_footnote = hospital_overall_rating_footnote
		self.__mortality_national_comparison = mortality_national_comparison
		self.__mortality_national_comparison_footnote = mortality_national_comparison_footnote
		self.__safety_of_care_national_comparison = safety_of_care_national_comparison
		self.__safety_of_care_national_comparison_footnote = safety_of_care_national_comparison_footnote
		self.__readmission_national_comparison = readmission_national_comparison
		self.__readmission_national_comparison_footnote = readmission_national_comparison_footnote
		self.__patient_experience_national_comparison = patient_experience_national_comparison
		self.__patient_experience_national_comparison_footnote = patient_experience_national_comparison_footnote
		self.__effectiveness_of_care_national_comparison = effectiveness_of_care_national_comparison
		self.__effectiveness_of_care_national_comparison_footnote = effectiveness_of_care_national_comparison_footnote
		self.__timeliness_of_care_national_comparison = timeliness_of_care_national_comparison
		self.__timeliness_of_care_national_comparison_footnote = timeliness_of_care_national_comparison_footnote
		self.__efficient_use_of_medical_imaging_national_comparison = efficient_use_of_medical_imaging_national_comparison
		self.__efficient_use_of_medical_imaging_national_comparison_footnote = efficient_use_of_medical_imaging_national_comparison_footnote
		self.__unnamed_28 = unnamed_28
		self.__hospital_number_of_reviews = hospital_number_of_reviews 
		self.__last_review = last_review
		self.__reviews_per_month = reviews_per_month
		self.__VIPcare_availability_365 = VIPcare_availability_365
		c.execute('''CREATE TABLE IF NOT EXISTS hospital (
			provider_id int PRIMARY KEY, 
			hospital_name varchar(52), 
			address varchar(52), 
			city varchar(52), 
			zip_code varchar(6),  
			phone_number varchar(13),  
			emergency_services varchar(3), 
			meets_criteria_for_meaningful_use_of_EHRs varchar(52),
			hospital_overall_rating varchar(52), 
			hospital_overall_rating_footnote varchar(52),
			mortality_national_comparison varchar(52),
			mortality_national_comparison_footnote varchar(52),
			safety_of_care_national_comparison varchar(52),
			safety_of_care_national_comparison_footnote varchar(52),
			readmission_national_comparison varchar(52),
			readmission_national_comparison_footnote varchar(52),
			patient_experience_national_comparison varchar(52),
			patient_experience_national_comparison_footnote varchar(52),
			effectiveness_of_care_national_comparison varchar(52),
			effectiveness_of_care_national_comparison_footnote varchar(52),
			timeliness_of_care_national_comparison varchar(52),
			timeliness_of_care_national_comparison_footnote varchar(52),
			efficient_use_of_medical_imaging_national_comparison varchar(52),
			efficient_use_of_medical_imaging_national_comparison_footnote varchar(52),
			unnamed_28 varchar(52), 
			hospital_number_of_reviews int, 
			last_review DATE,
			reviews_per_month int, 
			VIPcare_availability_365 int
		)''')

		if add:
			c.execute('''
				INSERT INTO hospital (
					provider_id, 
					hospital_name, 
					address, 
					city, 
					zip_code,  
					phone_number,  
					emergency_services, 
					meets_criteria_for_meaningful_use_of_EHRs,
					hospital_overall_rating, 
					hospital_overall_rating_footnote,
					mortality_national_comparison,
					mortality_national_comparison_footnote,
					safety_of_care_national_comparison,
					safety_of_care_national_comparison_footnote,
					readmission_national_comparison,
					readmission_national_comparison_footnote,
					patient_experience_national_comparison,
					patient_experience_national_comparison_footnote,
					effectiveness_of_care_national_comparison,
					effectiveness_of_care_national_comparison_footnote,
					timeliness_of_care_national_comparison,
					timeliness_of_care_national_comparison_footnote,
					efficient_use_of_medical_imaging_national_comparison,
					efficient_use_of_medical_imaging_national_comparison_footnote,
					unnamed_28, 
					hospital_number_of_reviews, 
					last_review,
					reviews_per_month, 
					VIPcare_availability_365)
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
				'''
			, (
				provider_id, 
				hospital_name, 
				address, 
				city,  
				zip_code,  
				phone_number, 
				emergency_services, 
				meets_criteria_for_meaningful_use_of_EHRs,
				hospital_overall_rating, 
				hospital_overall_rating_footnote,
				mortality_national_comparison,
				mortality_national_comparison_footnote,
				safety_of_care_national_comparison,
				safety_of_care_national_comparison_footnote,
				readmission_national_comparison,
				readmission_national_comparison_footnote,
				patient_experience_national_comparison,
				patient_experience_national_comparison_footnote,
				effectiveness_of_care_national_comparison,
				effectiveness_of_care_national_comparison_footnote,
				timeliness_of_care_national_comparison,
				timeliness_of_care_national_comparison_footnote,
				efficient_use_of_medical_imaging_national_comparison,
				efficient_use_of_medical_imaging_national_comparison_footnote,
				unnamed_28, 
				hospital_number_of_reviews, 
				last_review,
				reviews_per_month, 
				VIPcare_availability_365
				)
			)
			conn.commit()


	def get_provider_id(self): 
		return self.__provider_id

	def get_hospital_name(self):
		return self.__hospital_name

	def get_address(self):
		return self.__address

	def get_city(self):
		return self.__city

	def get_zip_code(self):
		return self.__zip_code

	def get_phone_number(self):
		return self.__phone_number

	def get_emergency_services(self): 
		return self.__emergency_services

	def get_meets_criteria_for_meaningful_use_of_EHRs(self):
		return self.__meets_criteria_for_meaningful_use_of_EHRs

	def get_hospital_overall_rating(self):
		return self.__hospital_overall_rating

	def get_hospital_overall_rating_footnote(self):
		return self.__hospital_overall_rating_footnote

	def get_mortality_national_comparison(self):
		return self.__mortality_national_comparison

	def get_mortality_national_comparison_footnote(self):
		return self.__mortality_national_comparison_footnote

	def get_safety_of_care_national_comparison(self):
		return self.__safety_of_care_national_comparison

	def get_safety_of_care_national_comparison_footnote(self):
		return self.__safety_of_care_national_comparison_footnote

	def get_readmission_national_comparison(self):
		return self.__readmission_national_comparison

	def get_readmission_national_comparison_footnote(self):
		return self.__readmission_national_comparison_footnote

	def get_patient_experience_national_comparison(self):
		return self.__patient_experience_national_comparison

	def get_patient_experience_national_comparison_footnote(self):
		return self.__patient_experience_national_comparison_footnote

	def get_effectiveness_of_care_national_comparison(self):
		return self.__effectiveness_of_care_national_comparison

	def get_effectiveness_of_care_national_comparison_footnote(self):
		return self.__effectiveness_of_care_national_comparison_footnote

	def get_timeliness_of_care_national_comparison(self):
		return self.__timeliness_of_care_national_comparison

	def get_timeliness_of_care_national_comparison_footnote(self):
		return self.__timeliness_of_care_national_comparison_footnote

	def get_efficient_use_of_medical_imaging_national_comparison(self):
		return self.__efficient_use_of_medical_imaging_national_comparison

	def get_efficient_use_of_medical_imaging_national_comparison_footnote(self):
		return self.__efficient_use_of_medical_imaging_national_comparison_footnote

	def get_unnamed_28(self):
		return self.__unnamed_28

	def get_hospital_number_of_reviews(self): 
		return self.__hospital_number_of_reviews

	def get_last_review(self):
		return self.__last_review

	def get_reviews_per_month(self): 
		return self.__reviews_per_month

	def get_VIPcare_availability_365(self):
		return self.__VIPcare_availability_365

	def set_provider_id(self, provider_id):
		self.__provider_id = provider_id
		c.execute("UPDATE hospital SET provider_id = ? WHERE id = ?", (provider_id, self.__provider_id))

	def set_hospital_name(self, hospital_name):
		self.__hospital_name = hospital_name
		c.execute("UPDATE hospital SET hospital_name = ? WHERE id = ?", (hospital_name, self.__provider_id))

	def set_address(self, address):
		self.__address = address
		c.execute("UPDATE hospital SET address = ? WHERE id = ?", (address, self.__provider_id))

	def set_city(self, city):
		self.__city = city
		c.execute("UPDATE hospital SET city = ? WHERE id = ?", (city, self.__provider_id))

	def set_zip_code(self, zip_code):
		self.__zip_code = zip_code
		c.execute("UPDATE hospital SET zip_code = ? WHERE id = ?", (zip_code, self.__provider_id))

	def set_phone_number(self, phone_number):
		self.__phone_number = phone_number
		c.execute("UPDATE hospital SET phone_number = ? WHERE id = ?", (phone_number, self.__provider_id))

	def set_emergency_services(self, emergency_services):
		self.__emergency_services = emergency_services
		c.execute("UPDATE hospital SET emergency_services = ? WHERE id = ?", (emergency_services, self.__provider_id))

	def set_meets_criteria_for_meaningful_use_of_EHRs(self, meets_criteria_for_meaningful_use_of_EHRs):
		self.__meets_criteria_for_meaningful_use_of_EHRs = meets_criteria_for_meaningful_use_of_EHRs
		c.execute("UPDATE hospital SET meets_criteria_for_meaningful_use_of_EHRs = ? WHERE id = ?", (meets_criteria_for_meaningful_use_of_EHRs, self.__provider_id))

	def set_hospital_overall_rating(self, hospital_overall_rating):
		self.__hospital_overall_rating = hospital_overall_rating
		c.execute("UPDATE hospital SET hospital_overall_rating = ? WHERE id = ?", (hospital_overall_rating, self.__provider_id))

	def set_hospital_overall_rating_footnote(self, hospital_overall_rating_footnote):
		self.__hospital_overall_rating_footnote = hospital_overall_rating_footnote
		c.execute("UPDATE hospital SET hospital_overall_rating_footnote = ? WHERE id = ?", (hospital_overall_rating_footnote, self.__provider_id))

	def set_mortality_national_comparison(self, mortality_national_comparison):
		self.__mortality_national_comparison = mortality_national_comparison
		c.execute("UPDATE hospital SET mortality_national_comparison = ? WHERE id = ?", (mortality_national_comparison, self.__provider_id))

	def set_mortality_national_comparison_footnote(self, mortality_national_comparison_footnote):
		self.__mortality_national_comparison_footnote = mortality_national_comparison_footnote
		c.execute("UPDATE hospital SET mortality_national_comparison_footnote = ? WHERE id = ?", (mortality_national_comparison_footnote, self.__provider_id))

	def set_safety_of_care_national_comparison(self, safety_of_care_national_comparison):
		self.__safety_of_care_national_comparison = safety_of_care_national_comparison
		c.execute("UPDATE hospital SET safety_of_care_national_comparison = ? WHERE id = ?", (safety_of_care_national_comparison, self.__provider_id))

	def set_safety_of_care_national_comparison_footnote(self, safety_of_care_national_comparison_footnote):
		self.__safety_of_care_national_comparison_footnote = safety_of_care_national_comparison_footnote
		c.execute("UPDATE hospital SET safety_of_care_national_comparison_footnote = ? WHERE id = ?", (safety_of_care_national_comparison_footnote, self.__provider_id))

	def set_readmission_national_comparison(self, readmission_national_comparison):
		self.__readmission_national_comparison = readmission_national_comparison
		c.execute("UPDATE hospital SET readmission_national_comparison = ? WHERE id = ?", (readmission_national_comparison, self.__provider_id))

	def set_readmission_national_comparison_footnote(self, readmission_national_comparison_footnote):
		self.__readmission_national_comparison_footnote = readmission_national_comparison_footnote
		c.execute("UPDATE hospital SET readmission_national_comparison_footnote = ? WHERE id = ?", (readmission_national_comparison_footnote, self.__provider_id))

	def set_patient_experience_national_comparison(self, patient_experience_national_comparison):
		self.__patient_experience_national_comparison = patient_experience_national_comparison
		c.execute("UPDATE hospital SET patient_experience_national_comparison = ? WHERE id = ?", (patient_experience_national_comparison, self.__provider_id))

	def set_patient_experience_national_comparison_footnote(self, patient_experience_national_comparison_footnote):
		self.__patient_experience_national_comparison_footnote = patient_experience_national_comparison_footnote
		c.execute("UPDATE hospital SET patient_experience_national_comparison_footnote = ? WHERE id = ?", (patient_experience_national_comparison_footnote, self.__provider_id))

	def set_effectiveness_of_care_national_comparison(self, effectiveness_of_care_national_comparison):
		self.__effectiveness_of_care_national_comparison = effectiveness_of_care_national_comparison
		c.execute("UPDATE hospital SET effectiveness_of_care_national_comparison = ? WHERE id = ?", (effectiveness_of_care_national_comparison, self.__provider_id))

	def set_effectiveness_of_care_national_comparison_footnote(self, effectiveness_of_care_national_comparison_footnote):
		self.__effectiveness_of_care_national_comparison_footnote = effectiveness_of_care_national_comparison_footnote
		c.execute("UPDATE hospital SET effectiveness_of_care_national_comparison_footnote = ? WHERE id = ?", (effectiveness_of_care_national_comparison_footnote, self.__provider_id))

	def set_timeliness_of_care_national_comparison(self, timeliness_of_care_national_comparison):
		self.__timeliness_of_care_national_comparison = timeliness_of_care_national_comparison
		c.execute("UPDATE hospital SET timeliness_of_care_national_comparison = ? WHERE id = ?", (timeliness_of_care_national_comparison, self.__provider_id))

	def set_timeliness_of_care_national_comparison_footnote(self, timeliness_of_care_national_comparison_footnote):
		self.__timeliness_of_care_national_comparison_footnote = timeliness_of_care_national_comparison_footnote
		c.execute("UPDATE hospital SET timeliness_of_care_national_comparison_footnote = ? WHERE id = ?", (timeliness_of_care_national_comparison_footnote, self.__provider_id))

	def set_efficient_use_of_medical_imaging_national_comparison(self, efficient_use_of_medical_imaging_national_comparison):
		self.__efficient_use_of_medical_imaging_national_comparison = efficient_use_of_medical_imaging_national_comparison
		c.execute("UPDATE hospital SET efficient_use_of_medical_imaging_national_comparison = ? WHERE id = ?", (efficient_use_of_medical_imaging_national_comparison, self.__provider_id))

	def set_efficient_use_of_medical_imaging_national_comparison_footnote(self, efficient_use_of_medical_imaging_national_comparison_footnote):
		self.__efficient_use_of_medical_imaging_national_comparison_footnote = efficient_use_of_medical_imaging_national_comparison_footnote
		c.execute("UPDATE hospital SET efficient_use_of_medical_imaging_national_comparison_footnote = ? WHERE id = ?", (efficient_use_of_medical_imaging_national_comparison_footnote, self.__provider_id))

	def set_unnamed_28(self, unnamed_28):
		self.__unnamed_28 = unnamed_28
		c.execute("UPDATE hospital SET unnamed_28 = ? WHERE id = ?", (unnamed_28, self.__provider_id))

	def set_hospital_number_of_reviews(self, hospital_number_of_reviews):
		self.__hospital_number_of_reviews = hospital_number_of_reviews
		c.execute("UPDATE hospital SET hospital_number_of_reviews = ? WHERE id = ?", (hospital_number_of_reviews, self.__provider_id))

	def set_last_review(self, last_review):
		self.__last_review = last_review
		c.execute("UPDATE hospital SET last_review = ? WHERE id = ?", (last_review, self.__provider_id))

	def set_reviews_per_month(self, reviews_per_month):
		self.__reviews_per_month = reviews_per_month
		c.execute("UPDATE hospital SET reviews_per_month = ? WHERE id = ?", (reviews_per_month, self.__provider_id))

	def set_VIPcare_availability_365(self, VIPcare_availability_365):
		self.__VIPcare_availability_365 = VIPcare_availability_365
		c.execute("UPDATE hospital SET VIPcare_availability_365 = ? WHERE id = ?", (VIPcare_availability_365, self.__provider_id))


class SQLWrapper():
	def __init__(self):
		pass

	def create_database(self, filename):
		self.df = pd.read_csv(filename)

		for x in self.df.columns:
			if self.df[x].dtype != "object":
				self.df[x] = self.df[x].astype('object')
		
		for row in self.df.to_records(index=False):
			h = Hospital(*row)

	def get_data(self, property, value):
		hospital_objects = []
		c.execute(f"SELECT * from hospital WHERE {property} = '{value}' ")
		hospitals = c.fetchall()
		for x in hospitals:
			hospital = x
			c.execute(f"SELECT * from state WHERE id = '{hospital[0]}' ")
			state = c.fetchone()
			c.execute(f"SELECT * from hospital_type WHERE id = '{hospital[0]}' ")
			hospital_type = c.fetchone()
			hospital_obj = Hospital(
				hospital[0],
				hospital[1],
				hospital[2],
				hospital[3],
				state[1],
				hospital[4],
				state[2],
				hospital[5],
				hospital_type[1],
				hospital_type[2],
				hospital[6],
				hospital[7],
				hospital[8],
				hospital[9],
				hospital[10],
				hospital[11],
				hospital[12],
				hospital[13],
				hospital[14],
				hospital[15],
				hospital[16],
				hospital[17],
				hospital[18],
				hospital[19],
				hospital[20],
				hospital[21],
				hospital[22],
				hospital[23],
				hospital[24],
				hospital[25],
				hospital[26],
				hospital[27],
				hospital[28],
				False
			)
			hospital_objects.append(hospital_obj)
		return hospital_objects

	def update_data(self, id, property, value):
		if property == 'state' or property == 'country_name':
			c.execute(f"UPDATE state SET {property} = '{value}' WHERE provider_id = '{id}'")
			conn.commit()
		elif property == "hospital_type" or property == "hospital_ownership":
			c.execute(f"UPDATE hospital_type SET {property} = '{value}' WHERE provider_id = '{id}'")
			conn.commit()
		else:
			c.execute(f"UPDATE hospital SET {property} = '{value}' WHERE provider_id = '{id}'")
			conn.commit()


	def delete_data(self, id):
		c.execute(f"DELETE from hospital_type WHERE id = '{id}'")
		c.execute(f"DELETE from state WHERE id = '{id}'")
		c.execute(f"DELETE from hospital WHERE provider_id = '{id}'")
		conn.commit()

if __name__ == '__main__':

	# Initialize wrapper object
	wrapper = SQLWrapper()

	# add csv data to the database
	# wrapper.create_database('DSA8002 (2021-2022)-dataset.csv')

	# Read data from the database table
	obj = wrapper.get_data(property = "provider_id", value="10001")
	print(obj[0].get_hospital_name(), obj[0].get_state())

	# Update data
	wrapper.update_data("10001", "hospital_name", "New Hospital")
	obj = wrapper.get_data(property = "provider_id", value="10001")
	print(obj[0].get_hospital_name(), obj[0].get_state())

	# delete record

	# wrapper.delete_data("230002")