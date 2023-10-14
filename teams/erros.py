from rest_framework.views import status
import ipdb
from .models import Team

class NegativeTitlesError(Exception):

    def _init_(self, massage, status_code):
        self.massage = massage
        self.status_code = status_code

    def valid_title(title):
        if title < 0:
            raise NegativeTitlesError({"error": "titlescannot be negative"}, status.HTTP_400_BAD_REQUEST)


class InvalidYearCupError(Exception):

    def _init_(self, massage, status_code):
        self.massage = massage
        self.status_code = status_code

    def valid_year(year):
        if year < 1930 or ((year - 1930) % 4) != 0:
            raise InvalidYearCupError({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)

class ImpossibleTitlesError(Exception):

    def _init_(self, massage, status_code):
        self.massage = massage
        self.status_code = status_code
    

    def valid_title(number_title, first_year, this_year):
        if number_title > ((this_year - first_year) / 4):
            raise ImpossibleTitlesError({"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST)

class NotfoundId(Exception):

    def _init_(self, massage, status_code):
        self.massage = massage
        self.status_code = status_code

    def cheack_id(tyeam_id):
        try:
            team = Team.objects.get(id=tyeam_id)
        except Team.DoesNotExist:
            raise NotfoundId({"error": "Team not found"}, status.HTTP_404_NOT_FOUND)
        return team