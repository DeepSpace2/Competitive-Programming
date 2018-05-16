# Solutions

## Crystal

```crystal
module RnaComplement
  def self.of_dna(dna : String)
    dna.gsub({'G' => 'C',
              'C' => 'G',
              'T' => 'A',
              'A' => 'U'})
  end
end
```