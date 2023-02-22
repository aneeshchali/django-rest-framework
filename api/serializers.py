from rest_framework import serializers



class PublicClassSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_table = serializers.SerializerMethodField(read_only=True)


    def get_other_table(self,obj):
        print(obj)
        return []