class PhysicsService:
    """A physics service inteface."""

    def has_collided(self, subject, agent):
        """Whether or not the given subject has collided with the given agent.
        
        Args:
            subject: An instance of Body.
            agent: An instance of Body.

        Returns:
            True if the subject has collided with the agent: false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_above(self, subject, agent):
        """Whether or not the given subject is above the given agent.
        
        Args:
            subject: An instance of Body.
            agent: An instance of Body.

        Returns:
            True if the subject is above the agent: false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_below(self, subject, agent):
        """Whether or not the given subject is below the given agent.
        
        Args:
            subject: An instance of Body.
            agent: An instance of Body.

        Returns:
            True if the subject is below the agent: false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_left_of(self, subject, agent):
        """Whether or not the given subject is to the left of the given agent.
        
        Args:
            subject: An instance of Body.
            agent: An instance of Body.

        Returns:
            True if the subject is to the left of the agent: false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_right_of(self, subject, agent):
        """Whether or not the given subject is to the right of the given agent.
        
        Args:
            subject: An instance of Body.
            agent: An instance of Body.

        Returns:
            True if the subject is to the right of the agent: false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")