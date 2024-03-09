screen_Rotationinfo=$(displayplacer list | grep -m 2 'Rotation' | tail -n 1)
rotation_number=$(echo $screen_Rotationinfo | awk '{print $2}')

# echo $rotation_number

# if [ "$rotation_number" = '0' ]; then
#     displayplacer "id:2 degree:90"  # 从0度顺时针旋转90度
# elif [ "$rotation_number" = '90' ]; then
#     displayplacer "id:2 degree:180"  # 从90度顺时针旋转90度

if [ "$rotation_number" = '0' ]; then
    displayplacer "id:2 origin:(1800,-1391) degree:270" 
else
    displayplacer "id:2 origin:(1800,-786) degree:0" 
fi


# displayplacer "id:2 origin:(1800,-1391)"(1800,-786)