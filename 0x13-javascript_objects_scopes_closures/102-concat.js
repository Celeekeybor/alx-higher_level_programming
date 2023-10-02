#!/usr/bin/node

'use strict';

const fileSystem = require('fs');

const firstArg = fileSystem.readFileSync(process.argv[2]).toString();
const secondArg = fileSystem.readFileSync(process.argv[3]).toString();
fileSystem.writeFileSync(process.argv[4], firstArg + secondArg);
