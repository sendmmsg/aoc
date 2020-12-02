#define _GNU_SOURCE
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define CHECK_BIT(var, pos) ((var) & (1 << (pos)))

int64_t get_usecs(void) {
  struct timespec ts;
  clock_gettime(CLOCK_MONOTONIC, &ts);
  return (int64_t)((int64_t)ts.tv_sec * 1000000 + (int64_t)ts.tv_nsec / 1000);
}

void find_two(int *val1, int *val2) {
  ssize_t len;
  ssize_t read;
  uint8_t exist[128];
  char buf[16];
  char *linebuf = &buf[0];
  int val;
  memset(exist, 0, 128);

  FILE *fp = fopen("input", "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);

  while ((read = getline(&linebuf, &len, fp)) != -1) {
    int ret = sscanf(linebuf, "%d", &val);
    if (ret != 1) {
      printf("Error scanning %s (val: %d)\n", linebuf, val);
      exit(EXIT_FAILURE);
    }
    // less than 1010, check if seen before or set
    if (val < 1010) {
      int bit = val % 8;
      int byte = val / 8;

      if (CHECK_BIT(exist[byte], bit)) {
        *val1 = val;
        *val2 = 2020 - val;
        goto exit;
      } else {
        exist[byte] |= 1 << bit;
      }
    } else {
      int orig = val;
      val = 2020 - orig;

      int bit = val % 8;
      int byte = val / 8;

      if (CHECK_BIT(exist[byte], bit)) {
        *val1 = val;
        *val2 = orig;
        goto exit;
      } else {
        exist[byte] |= 1 << bit;
      }
    }
  }
exit:
  fclose(fp);
}
void find_three(int *val1, int *val2, int *val3) {
  ssize_t len;
  ssize_t read;
  int values[200];
  char buf[16];
  char *linebuf = &buf[0];
  int val;

  FILE *fp = fopen("input", "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);
  int i = 0;
  while ((read = getline(&linebuf, &len, fp)) != -1) {
    int ret = sscanf(linebuf, "%d", &values[i]);
    if (ret != 1) {
      printf("Error scanning %s (val: %d)\n", linebuf, val);
      exit(EXIT_FAILURE);
    }
    i++;
  }
  fclose(fp);

  // could to the same as task one here, but.. pff
  for (i = 0; i < 200; i++) {
    for (int j = 0; j < 200; j++) {
      for (int k = 0; k < 200; k++) {
        if ((values[i] + values[j] + values[k]) == 2020) {
          *val1 = values[i];
          *val2 = values[j];
          *val3 = values[k];
          return;
        }
      }
    }
  }
}

int main(int argc, char **argv) {
  int64_t start = get_usecs();
  int val1, val2, val3;
  find_two(&val1, &val2);
  int64_t stop = get_usecs();
  printf("Task1: %d and %d (product: %d) (time: %ld microsec) \n", val1, val2,
         val1 * val2, stop - start);

  start = get_usecs();
  find_three(&val1, &val2, &val3);
  stop = get_usecs();
  printf("Task2: %d, %d, %d (product: %d) (time: %ld microsec) \n", val1, val2,
         val3, val1 * val2 * val3, stop - start);

  exit(EXIT_SUCCESS);
}
