
def count_batteries_by_usage(cycles): 
   a=0
   b=0
   c=0
   for i in range(len(cycles)):
      if cycles[i]<410:
        a+=1
      elif cycles[i]>=410 and cycles[i]<=949:
        b+=1
      else:
        c+=1
   return {
    "lowCount": a,
    "mediumCount": b,
    "highCount":c 
   }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
