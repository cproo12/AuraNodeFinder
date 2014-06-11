print "*******************************************************"
print "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
print "-_-_-_-_-_- THAUMCRAFT 4+ AURA NODE FINDER _-_-_-_-_-_-"
print "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
print "*******************************************************"

print "World Path should point at folder containing level.dat"
WORLDPATH = raw_input("Input World Save Path: ");

print "*******************************************************"
print "  "

import pymclevel
import sys
import os

try:
  world = pymclevel.mclevel.fromFile(WORLDPATH)
except IOError:
  sys.exit("IO error, check the world path")

chunks = list(world.allChunks)

if len(chunks) == 0:
  sys.exit("No chunks loaded?!")
print "Chunks loaded, now to find those nodes!"
print "  "
print "*******************************************************"
print "  "

for (xc,zc) in chunks:
  chunk = world.getChunk(xc,zc)
  for entity in chunk.TileEntities:
    if entity["id"].value == "TileNode":
      print(" %d y: %d z: %d") % (entity["x"].value, entity["y"].value, entity["z"].value)

print "  "
print "*******************************************************"
print "  "
print "Scanning Finished!"
print "  "
print "*******************************************************"
