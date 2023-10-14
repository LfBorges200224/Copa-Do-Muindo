import utils as utils
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from teams.models import Team

class TeamView(APIView):

    def post(self, request):
        teams_data = request.data 
        
        try:
            utils.data_processing(teams_data)
        except NegativeTitlesError as error:      
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        
        team = Team.objects.create(**teams_data) 

        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response :
        teams = Team.objects.all()

        teams_list = []    

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)


class TeamParamsView(APIView):

    def get(self, request:Request, team_id:int) -> Response:

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request:Request, team_id:int) -> Response:

        try:
           team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request:Request, team_id:int) -> Response:

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)