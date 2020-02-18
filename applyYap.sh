

for d in $(ls /Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/); 
do 
    echo $d;
    for f in $(ls /Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/$d);
        do
            echo $f;
            INPUTFILE="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/$d/$f"
            echo $INPUTFILE;
            LATTICEFILE="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/lattice/$d/$f.lattice"
            echo $LATTICEFILE;
            ../../../go/src/yap/yap hebma -raw $INPUTFILE -out $LATTICEFILE
            OUTPUTFILESEG="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/$d/$f.segmentation"
            OUTPUTFILEMAP="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/$d/$f.mapping"
            OUTPUTFILECON="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/$d/$f.conll"
            ../../../go/src/yap/yap joint -in $LATTICEFILE -os $OUTPUTFILESEG -om $OUTPUTFILEMAP -oc $OUTPUTFILECON
        done

done

