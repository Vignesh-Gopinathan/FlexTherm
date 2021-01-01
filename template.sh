root_dir=""$base""/cases/""
work_dir=""$base""/%temp%""
mkdir $work_dir
mkdir ""$root_dir""@1@""
cd ""$root_dir""@1@""
mkdir ""./""@2@""
cd "@2@"
mkdir ""./""@3@""
cd "@3@"
mkdir ""./""@4@""
cd "@4@"
save_dir=$(pwd)
cd $work_dir
cp -r ../base_case/* .
echo "COPIED FILES"
sed -i "s/#T_l#/%1%/g" constant/fluid/transportProperties
Ts=$(( Tl -  1 ))
sed -i "s/#T_s#/$Ts/g" constant/fluid/transportProperties
sed -i "s/#E_pot#/%2%/g" 0/global/Epot
sed -i "s/#Q_Heat#/-%3%/g" 0/global/T
sed -i "s/#el_bound#/%4%/g" system/fluid/setFieldsDict
echo "Setting fields"
# source /opt/OpenFOAM/OpenFOAM-4.1/etc/bashrc
# wait
setFields -region fluid
wait
echo "RUN SIMULATION"
globalMultiRegionThermoElectricTransientFoam &> log
wait
echo "FINISHED SIMULATION"
postProcess -func sampleDict -region fluid -latestTime
wait
echo "FINISHED PostProcess"
python3 createContour.py .
wait
python3 extractPropeT.py .
wait
# source /opt/openfoam7/etc/bashrc
# wait
# cp ../slice.py $work_dir
# wait
# pvpython slice.py $work_dir $save_dir
# wait
cd $save_dir
cp $work_dir/contour.csv .
wait
cp $work_dir/probeT.csv .
wait
# cp $work_dir/nohup.out .
cp $work_dir/log .
wait
cp -r $work_dir/postProcessing .
wait
rm -r $work_dir
cd $root_dir
echo "COMPLETED"

