

for d in $(ls /Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/); 
do 
    echo $d;
    INPUTDIR="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/$d/"
    LATTICEDIR="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/lattice/$d/"
    FINALRESDIR="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/$d/"
    mkdir -p $LATTICEDIR
    mkdir -p $FINALRESDIR
    for f in $(ls /Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/$d);
        do
            echo $f;
            INPUTFILE="$INPUTDIR$f"
            echo $INPUTFILE;
            LATTICEFILE="$LATTICEDIR$f.lattice"
            echo $LATTICEFILE;
            ../../../go/src/yap/yap hebma -raw $INPUTFILE -out $LATTICEFILE
            OUTPUTFILESEG="$FINALRESDIR$f.segmentation"
            OUTPUTFILEMAP="$FINALRESDIR$f.mapping"
            OUTPUTFILECON="$FINALRESDIR$f.conll"
            ../../../go/src/yap/yap joint -in $LATTICEFILE -os $OUTPUTFILESEG -om $OUTPUTFILEMAP -oc $OUTPUTFILECON
        done

done

# LATTICEDIR="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/lattice/amir/"
# FINALRESDIR="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/amir/"
# mkdir -p $LATTICEDIR
# mkdir -p $FINALRESDIR

# INPUTFILE="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/tokens/amir/0.0tokens.txt"
# echo $INPUTFILE;
# cat $INPUTFILE;
# LATTICEFILE="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/lattice/amir/0.0tokens.txt.lattice"
# echo $LATTICEFILE;
# ../../../go/src/yap/yap hebma -raw $INPUTFILE -out $LATTICEFILE
# OUTPUTFILESEG="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/amir/0.0tokens.txt.segmentation"
# OUTPUTFILEMAP="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/amir/0.0tokens.txt.mapping"
# OUTPUTFILECON="/Users/avsahar/school/Digitalhuman/DigitalHumanProject/finalresults/amir/0.0tokens.txt.conll"
# ../../../go/src/yap/yap joint -in $LATTICEFILE -os $OUTPUTFILESEG -om $OUTPUTFILEMAP -oc $OUTPUTFILECON

