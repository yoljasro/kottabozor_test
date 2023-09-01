import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Offers = () => {
  const [offers, setOffers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://www.kattabozor.uz/hh/test/api/v1/offers');
        setOffers(response.data.offers);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Offers</h1>
      {offers.map((offer) => (
        <div key={offer.id}>
          <h2>{offer.name}</h2>
          <p>Brand: {offer.brand}</p>
          <p>Category: {offer.category}</p>
          <p>Merchant: {offer.merchant}</p>
          <img src={offer.image.url} alt={offer.name} />
          <ul>
            {offer.attributes.map((attribute, index) => (
              <li key={index}>
                <strong>{attribute.name}:</strong> {attribute.value}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default Offers;