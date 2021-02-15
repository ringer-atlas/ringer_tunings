import os
basepath = os.getcwd()

path = basepath + '/Zrad/v1/r1'


command = """maestro.py task create \
  -v {PATH} \
  -t user.jodafons.mc16_13TeV.sgn.MC.gammajet.bkg.vetoMC.dijet.v1_et{ET}_eta{ETA}.r1 \
  -c user.jodafons.mc16_13TeV.sgn.MC.gammajet.bkg.vetoMC.dijet.v1_et{ET}_eta{ETA}.r0 \
  -d user.jodafons.mc16_13TeV.sgn.MC.gammajet.bkg.vetoMC.dijet_et{ET}_eta{ETA}.npz \
  --sd "{REF}" \
  --exec "run_reprocess.py -f %IN -d %DATA -r %REF -v %OUT -b zrad -t v1 -p r1" \
  --queue "gpu" """

try:
    os.makedirs(path)
except:
    pass

for et in range(5):
    for eta in range(5):
        ref = "{'%%REF':'user.jodafons.mc16_13TeV.sgn.MC.gammajet.bkg.vetoMC.dijet_et%d_eta%d.ref.pic.gz'}"%(et,eta)
        cmd = command.format(ET=et,ETA=eta,REF=ref,PATH=path)
        print(cmd)
        os.system(cmd)
        break
