import re
import sys
import task as t

class MyError(Exception):
    pass

def date_validity(userint):
            m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", userint) #-----------------Validation
            if not m:
                raise MyError("Expected YYYY-MM-DD format")
            return m

def month_valid(month):
     if month<1 or month>12 :
          raise MyError("Month must be between 1 and 12")
     else:
          return month

def day_valid(day):
     if day<1 or day>31:
            raise MyError("Day must be between 1 and 31")
     else:
          return day

def main():
    try:
        m = date_validity(input("Enter date in YYYY-MM-DD format: "))

        year, month, day = map(int, m.groups())

        month = month_valid(month)

        day = day_valid(day)
#------------------------------------------------------------------------------------------
        alt = int(input("Enter earth orbit altitude in km: "))
        if alt < 160:
            raise MyError("Minimum stable earth orbit is 160 km")
        target_alt = int(input("Enter moon orbit altitude in km: "))
        if target_alt < 1:
            raise MyError("Landing on moon is not supported")
        mass = int(input("Enter mass in kg: "))
        if mass < 1:
            raise MyError("Invalid mass")
        isp = int(input("Enter engine efficiency in seconds: "))
        if isp < 1:
            raise MyError("Invalid engine efficiency")

    except (ValueError, TypeError, MyError) as e:
        print("Invalid value/format in one of the inputs. Try again")
        print(f"{e}")
        sys.exit(1)
#=========================================================================================

    forecast, results = t.next_date(year, month, day, alt, target_alt)

    if forecast:
        fuel, deltav = t.calc_fuel(alt, results, isp, mass)

        print("Best launch day in next 30 days is...\n")
        print(f"{forecast}")
        print("================================")
        print(f"Flight time: {results['TOF']:.2f} DAYS")
        print(f"Phase angle: {results['Current_Phase']:.2f} degrees")
        print(f"Inclination: {results['Inc']:.2f} degrees")
        print("\n")
        print(f"Fuel Required: {fuel:.2f} kg")
        print(f"Delta v: {deltav*1000:.2f} m/s")

    else:
        print("No window found!")


if __name__ == "__main__":
    main()
