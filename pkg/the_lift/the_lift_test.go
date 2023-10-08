package thelift_test

// TODO: replace with your own tests (TDD). An example to get you started is included below.
// Ginkgo BDD Testing Framework <http://onsi.github.io/ginkgo/>
// Gomega Matcher Library <http://onsi.github.io/gomega/>

import (
	. "github.com/gabrielkenzo/codewars/pkg/the_lift"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Example tests", func() {
	It("My test", func() {
		Expect(TheLift([][]int{{}, {}, {5, 5, 5}, {}, {}, {}, {}}, 2)).To(Equal([]int{0, 2, 5, 0}))
	})
	It("Test up", func() {
		Expect(TheLift([][]int{{}, {}, {5, 5, 5}, {}, {}, {}, {}}, 5)).To(Equal([]int{0, 2, 5, 0}))
	})
	It("Test down", func() {
		Expect(TheLift([][]int{{}, {}, {1, 1}, {}, {}, {}, {}}, 5)).To(Equal([]int{0, 2, 1, 0}))
	})
	It("Test up and up", func() {
		Expect(TheLift([][]int{{}, {3}, {4}, {}, {5}, {}, {}}, 5)).To(Equal([]int{0, 1, 2, 3, 4, 5, 0}))
	})
	It("Test down and down", func() {
		Expect(TheLift([][]int{{}, {0}, {}, {}, {2}, {3}, {}}, 5)).To(Equal([]int{0, 5, 4, 3, 2, 1, 0}))
	})
})
