# Getting started

### Step 1: stake in UI
see: https://dashboard.threshold.network/overview/network

### Step 2: generate key material
```
bash scripts/create-key-material.sh
```

XXX BACK THIS UP SOMEPLACE SAFE!!!!!

### Step 3: generate operator key

Create a secure password for your operator account
```
bash scripts/generate-password.sh
```

Submit the password you just generated when prompted
```
geth account new --datadir ./
```

NOTE: this will need to be funded with eth!!!


### Step 4: generate password for nucypher keystore

Generate another password for the nucypher keystore
```
bash scripts/generate-password.sh
```

### Step 5: 

bond the operator address you generated with the address that controls your T (or legacy nu/keep) stake: https://stake.nucypher.network/manage/bond

### Step 6: Install Dappnode package

Release hash : /ipfs/QmZWVtYFfSkPSGrjvrDw5YVCzmDQtduC1fu5FGHZLn5zhh
http://my.dappnode/#/installer/%2Fipfs%2FQmZWVtYFfSkPSGrjvrDw5YVCzmDQtduC1fu5FGHZLn5zhh

and fill in the environment variables


### Step 7: Backup the data directories
Using the Backup tab on the package's page


# Installing prebuilt package
Note the security assumptions you are making when you install software you didn't build from source!

```
Release hash : /ipfs/QmbDSazBXxfv7R4fkqGBd5JLRqQk2vtBDzpAMy3YGwKdFF
```
goto http://my.dappnode/#/installer/%2Fipfs%2FQmbDSazBXxfv7R4fkqGBd5JLRqQk2vtBDzpAMy3YGwKdFF
on your dappnode vpn or wifi network

# Building from source
better to build your own from source:
```
dappnodesdk build
```