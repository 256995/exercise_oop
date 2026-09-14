from mimetypes import inited


class GenomicFeature:
    def __init__(self, chromosome, start, end, strand):
        # check validity of variables and assign to the object
        if isinstance(chromosome, str):
            self.chromosome = chromosome
        else:
            print("Error: Chromosome must be a string.")
        if isinstance(start, int) and isinstance(end, int):
            if start >= 1 or end >= start:
                self.start = start
                self.end = end
            else:
                print("Error: Start or end values are not valid.")
        else:
            print("Error: Start and end must be integers.")
        if (strand == "-") or (strand == "+"):
            self.strand = strand
        else:
            print("Error: Strand must be either '+' or '-'.")
    # should use raise instead of print, but currently I don't know, how it works

    def length(self):
        return self.end - self.start + 1

    def overlaps(self, other):
        if self.chromosome == other.chromosome:
            if (self.start <= other.start <= self.end) or (other.start <= self.start <= other.end):
                return True
            else:
                return False
        else:
            return False

    def describe(self):
        return f"{type(self).__name__} {self.chromosome}: {self.start}-{self.end}({self.strand})"


class Exon(GenomicFeature):
    def __init__(self, chromosome, start, end, strand, exon_number):
        super().__init__(chromosome, start, end, strand)
        if isinstance(exon_number, int):
            self.exon_number = exon_number
        else:
            print("Error: Exon_number must be an integer.")

    def describe(self):
        return f"{type(self).__name__} {self.chromosome}: {self.start}-{self.end}({self.strand}),no.: {self.exon_number}"

if __name__ == "__main__":
    a = GenomicFeature("chr1", 1000, 5000, "+")
    b = GenomicFeature("chr1", 4800, 6000, "+")
    c = GenomicFeature("chr2", 1000, 5000, "+")

    print(a.describe())
    print(a.length())
    print(a.overlaps(b))
    print(a.overlaps(c))
    GenomicFeature("chr1", 5000, 1000, "+")

    features = [
        GenomicFeature("chr1", 1000, 5000, "+"),
        Exon("chr1", 1000, 1200, "+", 1),
        Exon("chr1", 3000, 3300, "+", 2),
    ]
    for feature in features:
        print(feature.describe())