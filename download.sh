#/bin/sh

mkdir -p ./data

for i in `seq 1 4`; do
  ZIP="G$i.zip"
  curl $RP_BASEURL/$ZIP -u $RP_USER:$RP_PASS -o ./data/$ZIP -s
  unzip -d ./data -q ./data/$ZIP
  rm ./data/$ZIP
done
