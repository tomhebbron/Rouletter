
#include <cstddef>
#include <vector>

namespace Rouletter
{


    // A Rouletter class keeps the bounds as a private property (so avoids moving the array to and from python)
    template<typename T> class Rouletter
    {
        private:
            const size_t len;
            double *bounds;

        public:

            Rouletter(const std::vector<T> &data) : len(data.size())
            {
                this->bounds = new double[this->len];
                rouletter_init(data,this->bounds);
            }

            Rouletter(const T *data, const size_t len) : len(len)
            {
                this->bounds = new double[len];
                rouletter_init(data,len,this->bounds);
            }

            ~Rouletter() {delete[] bounds;}


            // rouletter_init sets up the array of bounds given data. You pass in a array of ints, a pointer to an array of doubles to use as the bounds.
            static void rouletter_init(const T* data, const size_t len, double* bounds)
            {
                double sum = 0.0, bound = 0.0;
                //sum data
                for(size_t i=0; i<len; ++i)
                {
                    sum += data[i];
                }

                //set boundaries
                for(size_t i=0; i<len; ++i)
                {
                    bound += (data[i] / sum);
                    bounds[i] = bound;
                }
            }

            static void rouletter_init(const std::vector<T>& data, double* bounds)
            {
                rouletter_init(&data[0], data.size(), bounds);
            }


            // rouletter_spin spins the wheel and returns the index of the lucky slot. bounds is as calculated by rouletter_init, len is length of array, luck is [0->1] random number.
            static size_t rouletter_spin(const double *bounds, const size_t len, const double luck)
            {
                for (size_t i=0; i<len; ++i) if (bounds[i] > luck) return i;
                return len;
            }


            // rouletter_spin_bisect is a variant that bisects the bounds array for higher performance when testing where luck lands.
            static size_t rouletter_spin_bisect(const double *bounds, const size_t len, const double luck)
            {
                int lo = 0, mid = 0, hi = len;
                while (lo < hi)
                {
                    mid = (lo+hi)/2; // floor division (remainder is discarded)
                    if (bounds[mid] < luck) lo = mid+1;
                    else hi = mid;
                }
                return lo;
            }


            inline size_t spin(const double luck)
            {
                return rouletter_spin(this->bounds,this->len,luck);
            }

            inline size_t spin_bisect(const double luck)
            {
                return rouletter_spin_bisect(this->bounds,this->len,luck);
            }







    };

    class RouletterI : public Rouletter<int> {};

    class RouletterD: public Rouletter<double> {};




};




