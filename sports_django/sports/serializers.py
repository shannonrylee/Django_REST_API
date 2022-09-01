from rest_framework import serializers
from .models import Team , Player

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Team
        fields = ('id', 'photo_url', 'league', 'name', 'city')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
        players = serializers.HyperlinkedModelSerializer(
            view_name ='team_detail',
            read_only=True
        )
        class Meta:
            model = Player
            fields = ('id', 'name', 'position', 'injured')